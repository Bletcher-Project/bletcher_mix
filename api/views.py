import io
from cloudinary.uploader import upload
import torchvision.transforms as transforms
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import neural_style as ns


@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful",
    }
    return Response(return_data)


@api_view(['POST'])
def bletcher_mix(request):
    try:
        content_url = request.data.get('content_image_path', None)
        style_url = request.data.get('style_image_path', None)
        mix_image_name = request.data.get('mix_image_name', None)
        
        fields = [content_url, style_url, mix_image_name]

        if not None in fields:
            print("content url : {}".format(content_url))
            print("style url : {}".format(style_url))
            print("output name : {}".format(mix_image_name))

            cnn, cnn_normalization_mean, cnn_normalization_std, style_img, content_img, input_img = ns.set_neural_style(
                content_url, style_url)

            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                           content_img, style_img, input_img)

            tensor_img = output[0].squeeze(0)

            output_name = mix_image_name
            print("output name : {}\n".format(output_name))

            transformer = transforms.ToPILImage()
            save_image = transformer(tensor_img)

            byteIO = io.BytesIO()
            save_image.save(byteIO, format='jpeg')
            byteArr = byteIO.getvalue()

            res = upload(byteArr, folder="post/mix", public_id=output_name)

            if res:
                result = {
                    'error': 0,
                    'message': 'Successful',
                    'name': output_name,
                    'type': ("{}/{}".format(res['resource_type'], res['format'])),
                    'path': res['secure_url']
                }
                resStatus = status.HTTP_200_OK
        else:
            result = {
                'error': 1,
                'message': 'Invalid Parameters'
            }
            resStatus = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        result = {
            'error': 2,
            "message": str(e)
        }
        resStatus = status.HTTP_500_INTERNAL_SERVER_ERROR

    print("Response : {}\n".format(result))
    return Response(result, status=resStatus)
