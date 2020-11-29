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
# Create your views here.


@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful",
    }
    return Response(return_data)


@api_view(["POST"])
def bletcher_mix(request):
    try:
        content_url = request.data.get('content_url', None)
        style_url = request.data.get('style_url', None)

        fields = [content_url, style_url]

        #
        print("try문 완료")
        #

        if not None in fields:
            # Datapreprocessing Convert the values to float
            content_url = str(content_url)
            style_url = str(style_url)

            print("content : {}".format(content_url))
            print("style : {}".format(style_url))

            cnn, cnn_normalization_mean, cnn_normalization_std, style_img, content_img, input_img = ns.set_neural_style(
                content_url, style_url)
            
            # output : 3차원 tensor array
            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                           content_img, style_img, input_img)
            
            # tensor_img : 2차원 tensor array
            tensor_img = output[0].squeeze(0)
            
            # output_name : 저장할 파일 이름
            output_name = '{}x{}1.jpg'.format(style_url, content_url)
            
            print("1")
            unloader = transforms.ToPILImage()
            save_image = unloader(tensor_img)      # 아까 생성했던 fake batch 삭제

            print("2")
            byteIO = io.BytesIO()
            print("2-1")
            save_image.save(byteIO, format='jpeg')
            print("2-2")
            byteArr = byteIO.getvalue()
            print("2-3")
            
            # save_image : 로컬 파일시스템에 이미지 파일로 저장하는 함수
            # 실제 heroku에서는 로컬 파일시스템을 사용할 수 없으므로, save_image를 사용할 수 없습니다.
            # from torchvision.utils import save_image
            #save_image(tensor_img, '/Users/yungoing/Desktop/bletcher/bletcher_mix/api/data/output/{}'.format(output_name))
            
            # cloudinary에 업로드하는 함수 : upload([file], foler=[target dir])
            # 이 때 [file] <- 이 부분이 file type이어야 하는데, tensor array라 해결이 안 되는 부분입니다.
            
            # save_image = Image.fromarray(tensor_img.)
            cloudinary.uploader.upload(byteArr, folder="post/")

            print("3")
            
            result = {
                'error': '0',
                'message': 'Successfull',
                'output_name': output_name
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
