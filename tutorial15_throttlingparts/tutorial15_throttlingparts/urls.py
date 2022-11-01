
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/',views.studentList.as_view()),#get data all
    # path('student/',views.studentLS.as_view()),#get data all
    # path('student/',views.studentCreate.as_view())
    # path('student/<int:pk>',views.studentRetrive.as_view())
    # path('student/<int:pk>',views.studentUpdate.as_view())
    path('student/<int:pk>',views.studentDestroy.as_view())
    # path('student/<int:pk>',views.studentRUD.as_view())
 
]
