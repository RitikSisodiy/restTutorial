
from django.contrib import admin
from django.urls import path
from apiview import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.hello)
]
