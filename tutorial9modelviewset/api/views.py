from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets
#modelviewset
# class studentModelViewset(viewsets.ModelViewSet):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

# read only model view set you can only read update and retrieve method is not working
class studentModelViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
