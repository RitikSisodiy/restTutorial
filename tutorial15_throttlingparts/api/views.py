#concret views classes
from .models import student
from .serializers import studentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class studentList(ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
class studentCreate(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'
class studentRetrive(RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
class studentUpdate(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'
class studentDestroy(DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'
