from django.contrib import admin
from .models import student,blog,relation
# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name' ,'roll' , 'city']
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['id']
@admin.register(relation)
class relationAdmin(admin.ModelAdmin):
    list_display = ['id',"student","blog","t"]