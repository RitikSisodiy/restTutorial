#genericapi view and model mixin
from .models import student
from .serializers import studentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# list and create PK is not required
class LCstudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    def get(self , request , *args ,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self , request , *args ,**kwargs):
        return self.create(request,*args,**kwargs)
# RETEIVE , UPDATE and DELETE PK is  required
class RUDstudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def get(self , request , *args ,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self , request , *args ,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self , request , *args ,**kwargs):
        return self.destroy(request,*args,**kwargs)


