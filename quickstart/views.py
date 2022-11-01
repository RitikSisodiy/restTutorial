from django.shortcuts import render
from io import BytesIO
from . models import student
from .serializers import studentSerializer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        try:
            stream = BytesIO(json_data)
            pythondata = JSONParser().parse(stream) 
        except:
            pythondata = {}
        id = pythondata.get('id',None)
        if id is not None:
            stu = student.objects.filter(id = id)
            if len(stu)>0:
                serializer = studentSerializer(stu[0]).data
            else:
                res = {'msg':'record id is not exist '}
                serializer = JSONRenderer().render(res)
        else:
            stu = student.objects.all()    
            serializer = studentSerializer(stu,many =True).data
        json_data = JSONRenderer().render(serializer)
        return HttpResponse(json_data,content_type = 'application/json')
    if request.method == "POST":
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'record is created seccessfully id is ' + str(serializer.save().id)}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            json_data = json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
    if request.method == "PUT":
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id = id)
        serializer = studentSerializer(stu , data=pythondata , partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'record is updated '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            json_data = json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
    if request.method == "DELETE":
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            try:
                student.objects.get(id = id).delete()
                res = {'msg':'record is deleted '}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type = 'application/json')
            except Exception as e:
                res = {'msg':'record id is not exitst '}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type = 'application/json')
