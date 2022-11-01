from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

#creating router object
router = DefaultRouter()
router.register('student',views.studentModelViewset,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls )),
    path('gettoken/',TokenObtainPairView.as_view(), name = 'token_obtain_pair'),# default validity 5 min
    path('refreshtoken/',TokenRefreshView.as_view(), name = 'token_refresh_pair'),# default validity 1 day
    path('verifytoken/',TokenVerifyView.as_view(), name = 'token_verify_pair'),
]
