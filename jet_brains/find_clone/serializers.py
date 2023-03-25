from rest_framework import serializers
from .models import New_File


class New_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_File
        fields = '__all__'