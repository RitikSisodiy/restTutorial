from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST','GET'])
def hello(request):
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'this is post request','data':request.data})
    return Response({'msg':'this is get request'})