
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.studentList.as_view()),#get data all
    # path('student/',views.studentCreate.as_view()),# create data
    # path('student/<int:pk>',views.studentRetrive.as_view())  # retrive single daata
    path('student/<int:pk>',views.studentUpdate.as_view())  # Update data
    # path('student/<int:pk>',views.studentDistroy.as_view())  # delete data
]
