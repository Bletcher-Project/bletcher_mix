# Import necessary libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
from api import neural_style as ns

from PIL import Image
from torchvision.utils import save_image
import torchvision.transforms as transforms
import cloudinary
import cloudinary.api
import cloudinary.uploader
import io
from urllib.request import urlopen
import ssl


# Create your views here.


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

            # output : 3차원 tensor array
            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                           content_img, style_img, input_img)

            # tensor_img : 2차원 tensor array
            tensor_img = output[0].squeeze(0)

            # output_name : 저장할 파일 이름
            output_name = "{}".format(mix_image_name)
            print("output name : {}\n".format(output_name))

            unloader = transforms.ToPILImage()
            save_image = unloader(tensor_img)  # fake batch 삭제

            byteIO = io.BytesIO()
            save_image.save(byteIO, format='jpeg')
            byteArr = byteIO.getvalue()

            # cloudinary에 업로드
            res = cloudinary.uploader.upload(byteArr, folder="post/mix", public_id=output_name)
            result = {
                'error': '0',
                'message': 'Successful',
                'name': output_name,
                'type': ("{}/{}".format(res['resource_type'], res['format'])),
                'path': res['secure_url']
            }
        else:
            result = {
                'error': '1',
                'message': 'Invalid Parameters'
            }
    except Exception as e:
        result = {
            'error': '2',
            "message": str(e)
        }

    return Response(result)
