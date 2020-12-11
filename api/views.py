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


@api_view(['POST'])
def bletcher_mix(request):
    try:
        content_url = request.data.get('content_url', None)
        style_url = request.data.get('style_url', None)

        fields = [content_url, style_url]


        if not None in fields:
            print()
            print("url find")
            print()

            # Datapreprocessing Convert the values to float
            content_url = str(content_url)
            style_url = str(style_url)

            print("content : {}".format(content_url))
            print("style : {}".format(style_url))
            print()
            
            cnn, cnn_normalization_mean, cnn_normalization_std, style_img, content_img, input_img = ns.set_neural_style(
                content_url, style_url)
            
            # output : 3차원 tensor array
            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                           content_img, style_img, input_img)
            
            # tensor_img : 2차원 tensor array
            tensor_img = output[0].squeeze(0)
            
            # output_name : 저장할 파일 이름
            output_name = '{}x{}1.jpg'.format(style_url, content_url)
            print("output name : {}".format(output_name))
            print()

            unloader = transforms.ToPILImage()
            save_image = unloader(tensor_img)      # 아까 생성했던 fake batch 삭제

            byteIO = io.BytesIO()
            save_image.save(byteIO, format='jpeg')
            byteArr = byteIO.getvalue()

            # cloudinary에 업로드
            cloudinary.uploader.upload(byteArr, folder="post/")
            
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
