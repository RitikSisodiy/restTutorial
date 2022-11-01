#concret views classes
from .models import student
from .serializers import studentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


class studentList(ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class studentCreate(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
class studentRetrive(RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
class studentUpdate(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
class studentDestroy(DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
class studentLS(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
class studentRUD(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
