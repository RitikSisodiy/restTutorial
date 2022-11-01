from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# modelviewset

class studentModelViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
class studentModelViewset1(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]# user can use if staff status is true
class studentModelViewset2(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]