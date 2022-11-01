from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == "GET":
        id  = request.data.get('id')
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
        id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            serializer = studentSerializer(stu,data=request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'data updated!!! '})
            return Response(serializer.errors)
        return Response({"msg":"id is required"})
    if request.method == 'DELETE':
        id = request.data.get('id')
        if id is not None:
            stu = student.objects.get(id = id)
            stu.delete()
            return Response({"msg":"data is deleted !!!"})
        return Response({"msg":"id is required"})
        