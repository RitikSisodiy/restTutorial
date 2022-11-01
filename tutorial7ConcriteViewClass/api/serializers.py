from rest_framework import serializers
from . models import student
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id','name','roll','city']
    def validate_name(self,value):
        if len(value)>15:
            raise serializers.ValidationError("name should be less than 15 character")
        return value