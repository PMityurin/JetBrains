from django.shortcuts import render
from .forms import UserForm
from django import forms
from django.core.files.storage import FileSystemStorage
from .logiс import new_token, file_comparison

from rest_framework import viewsets

from .models import  New_File


# processing the file received from the form
def index(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        new_token(fs.url(filename))
        file_info = file_comparison(fs.url(filename))
        return render(request, 'layout.html', {
            'info': file_info
        })
    else:
        userform = UserForm()
        return render(request, 'layout.html')
