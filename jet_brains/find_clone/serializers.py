from rest_framework import serializers
from .models import Result, New_File


# class All_infoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = All_info
#         fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class New_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_File
        fields = '__all__'