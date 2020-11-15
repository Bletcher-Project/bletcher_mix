#Import necessary libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
from api import neural_style as ns
from torchvision.utils import save_image

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def bletcher_mix(request):
    try:
        content_url = request.data.get('content_url',None)
        style_url = request.data.get('style_url',None)
        
        fields = [content_url, style_url]

        if not None in fields:
            #Datapreprocessing Convert the values to float
            content_url = str(content_url)
            style_url = str(style_url)
            
            cnn, cnn_normalization_mean, cnn_normalization_std, style_img, content_img, input_img = ns.set_neural_style(content_url, style_url)
            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,\
                content_img, style_img, input_img)

            save_img = output[0]
            output_name = '{}x{}.jpg'.format(style_url, content_url)
            save_image(save_img, '/Users/yungoing/Desktop/bletcher/bletcher_mix/api/data/output/{}'.format(output_name))


            #print('synthesizing')
            result = {
                'error' : '0',
                'message' : 'Successfull',
                'output_name' : output_name
            }
        else:
            result = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        result = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(result)