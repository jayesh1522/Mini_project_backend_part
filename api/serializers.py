from dataclasses import fields
from rest_framework import serializers

from .models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserInfo
        fields=("__all__")
        
        
        
        
class MedicineSerializer(serializers.ModelSerializer):
    # person=serializers.SerializerMethodField()
    
    class Meta:
        model=Medicine
        fields=("__all__")
        
    # def get_person(self,obj):
    #     query=UserInfo.objects.filter(name=obj.person)
    #     serializer=UserInfoSerializer(query, many=True).data[0]
    #     return serializer
    
    
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalRecord
        fields=("__all__")