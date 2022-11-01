
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.LCstudentAPI.as_view()),#get data all
    path('student/<int:pk>',views.RUDstudentAPI.as_view())  # Update data
    # path('student/<int:pk>',views.studentDistroy.as_view())  # delete data
]
