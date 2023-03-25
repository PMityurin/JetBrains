from .models import Result, New_File
from rest_framework import viewsets, permissions, status
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ResultSerializer, New_fileSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def find_clone_list(request):
#     if request.method == "GET":
#         new_file = New_File.objects.all()
#         serializer = New_fileSerializer(new_file, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = New_fileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(ResultSerializer.data, safe=False)
#         return JsonResponse(ResultSerializer.errors, safe=False)


# class All_infoViewSet(viewsets.ModelViewSet):
#     permission_classes = [
#             permissions.AllowAny
#         ]
#     queryset = All_info.objects.all().order_by('-id')
#     serializer_class = All_infoSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().order_by('-new_file_id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResultSerializer


class New_FileViewSet(viewsets.ModelViewSet):
    queryset = New_File.objects.all().order_by('-id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = New_fileSerializer

