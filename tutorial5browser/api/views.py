from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
from rest_framework import status
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk= None):
    if request.method == "GET":
        if pk is not None:
            id = pk
        else:
            id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu)
            return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
        stu = student.objects.all()
        serializer =  studentSerializer(stu, many = True)
        return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)
    if request.method == "POST":
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "record created id is "+ str(serializer.save().id)},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        if pk is not None:
            id = pk
        else:
            id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updated!!! '},status=status.HTTP_201_CREATED )
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg":"id is required"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        if pk is not None:
            id = pk
        else:
            id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu,data=request.data,partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updated!!! '},status=status.HTTP_201_CREATED )
            return Response(serializer.errors)
        return Response({"msg":"id is required"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        if pk is not None:
            id = pk
        else:
            id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            stu.delete()
            return Response({"msg":"data is deleted !!!"},status=status.HTTP_200_OK)
        return Response({"msg":"id is required"},status= status.HTTP_400_BAD_REQUEST)
        