from django.contrib.auth.models import User , Group
from rest_framework import serializers
from . models import student
#two ways to make serilizer
#model class serilizers
class studentSerializer(serializers.ModelSerializer): # 1st way in this way there is no need to create update and create method of funtion
    #custum validater
    # def start_with_r(value):
    #     if value[0].lower()!= 'r':
    #         raise serializers.ValidationError('name should start with R')
    # name = serializers.CharField(validators= [start_with_r]) # validation cant be change read only
    class Meta:
        model = student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','city']
        # extra_kwargs = {'name':{'read_only':True}} # add property 

# validation in model serilizer
    # 1 field level validation
    # def validate_name(self,value):
    #     if len(value)>15:
    #         raise serializers.ValidationError("name should be less than 15 chareacter")
    #     return value
    
    # 2 object level validation
    # def validate(self,data):
    #     name = data.get('name','')
    #     if len(name)>15:
    #         raise serializers.ValidationError("name should be be less than 15 character")
    #     return data

# class studentSerializer(serializers.Serializer):  # 2nd way
#     # foo fetch the data
#     id = serializers.ReadOnlyField()
#     # name = serializers.CharField(max_length = 100 ,validators= [start_with_r])  # custum validater
#     name = serializers.CharField(max_length = 100 ,)  
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#     #  for creating the new record