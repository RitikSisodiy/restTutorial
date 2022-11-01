from django.shortcuts import render
from rest_framework.response import Response
from . models import student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework import viewsets

class studentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=  student.objects.all()
        serializer = studentSerializer(stu,many = True)
        return Response(serializer.data)
    def create(self,request):
        stu=  student.objects.all()
        serializer = studentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    def retrieve(self,request, pk =None):
        if pk is not None:
            stu=  student.objects.get(id =pk)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
        return Response({'msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk= None):
        if pk is not None:
            stu=  student.objects.get(id = pk)
            serializer = studentSerializer(stu,data= request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({'msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk= None):
        if pk is not None:
            student.objects.get(id = pk).delete()
            return Response({'msg':'data deleted'})
        return Response({'msg':'bad request'},status=status.HTTP_400_BAD_REQUEST)
