from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .authtoken import CustumAuthToken

#creating router object
router = DefaultRouter()
router.register('student',views.studentModelViewset,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls )),
    path('auth/', include('rest_framework.urls'),name= 'restframe_work'),
    # path('gettoken/', obtain_auth_token)#bulit in method
    path('gettoken/',CustumAuthToken.as_view() )# if you want to return extra details create custum token class
]
