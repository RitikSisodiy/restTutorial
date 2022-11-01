from django.contrib.auth.models import User , Group
from rest_framework import serializers
from . models import student
# make custum validater
def start_with_r(value):
    print(value[0].lower())
    if value[0].lower() != 'r':
        raise serializers.ValidationError("name should start with R") 
    return value
class studentSerializer(serializers.Serializer):
    # foo fetch the data
    id = serializers.ReadOnlyField()
    # name = serializers.CharField(max_length = 100 ,validators= [start_with_r])  # custum validater
    name = serializers.CharField(max_length = 100 ,)  
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    #  for creating the new record
    
    def create(self, validated_data):
        return student.objects.create(**validated_data)
    #  for updating existing recording
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    # field level validation use for single field validation
    # def validate_name(self, value):
    #     if len(value)>15:
    #         raise serializers.ValidationError("name should be less than 15 character")
    #     else:
    #         return value
    

    # object level validation use for all field in object
    # def validate(self, data):
    #     name = data.get('name','')
    #     city = data.get('city','')
    #     if city == 'dhar':
    #         raise serializers.ValidationError('city dhar is not required')
    #     if len(name)>15:
    #         raise serializers.ValidationError('name should be less than 15 character')
    #     return data