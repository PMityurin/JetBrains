from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django import forms
from django.core.files.storage import FileSystemStorage
from .logika import new_token, file_comparison
# Create your views here.


def index(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        new_token(fs.url(filename))
        file_url = file_comparison()
        return render(request, 'layout.html', {
            'info': file_url
        })
        # return HttpResponse(f"<h2> title {title} - Тут будет ответ {file}, {type(file)}</h2>")
    else:
        userform = UserForm()
        return render(request, 'layout.html')
# def check_new_file_view(request):
#     '''Веб-сервис, обрабатывающий новый файл.
#     Разбивает его на токены и сравнивает с уже имеющимися'''
#     new_file = request.POST.files
#     with open(new_file, 'r') as new_f:
#
#     return JsonResponse({'success': True})