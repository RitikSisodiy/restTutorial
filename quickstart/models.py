from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class blog(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class relation(models.Model):
    student = models.ForeignKey(student,on_delete=models.SET_NULL,null=True,related_name="srelation")
    blog = models.ForeignKey(blog,on_delete=models.SET_NULL,null=True,related_name="brelation")
    t = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return str(self.id)
