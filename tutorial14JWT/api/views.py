from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# four ways to create token
# 1 : in admin pannal add Token
# 2 : from command line run drf_create_token <username> return token in exist or create newone
# 3 : user can create token api exposing api endpoint
# 4 : using signals


# modelviewset

class studentModelViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]