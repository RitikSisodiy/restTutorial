from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny,DjangoModelPermissions
# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([DjangoModelPermissions])
def student_api(request,pk = None):
    if pk is not None:
        id = pk
    else:
        id  = request.data.get('id')
    if request.method == "GET":
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer =  studentSerializer(stu, many = True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "record created id is "+ str(serializer.save().id)})
        return Response(serializer.errors)
    if request.method == 'PUT':
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu,data=request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updated!!! '})
            return Response(serializer.errors)
        return Response({"msg":"id is required"})
    if request.method == 'DELETE':
        if id is not None:
            stu = student.objects.get(id = id)
            stu.delete()
            return Response({"msg":"data is deleted !!!"})
        return Response({"msg":"id is required"})
        