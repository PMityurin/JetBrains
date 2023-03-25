from .models import New_File
from rest_framework import viewsets, permissions
from .serializers import New_fileSerializer


class New_FileViewSet(viewsets.ModelViewSet):
    queryset = New_File.objects.all().order_by('-id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = New_fileSerializer

