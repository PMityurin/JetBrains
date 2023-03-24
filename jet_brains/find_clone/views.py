from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django import forms
from django.core.files.storage import FileSystemStorage
from .logiс import new_token, file_comparison

from rest_framework import viewsets

from .serializers import New_FileSerializer
from .models import  New_File


class New_FileSet(viewsets.ModelViewSet):
    queryset = New_File.objects.all()
    serializer_class = New_FileSerializer


def index(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        new_token(fs.url(filename))
        file_info = file_comparison(fs.url(filename))
        return render(request, 'layout.html', {
            'info': file_info
        })
    else:
        userform = UserForm()
        return render(request, 'layout.html')
