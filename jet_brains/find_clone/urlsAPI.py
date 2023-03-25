from rest_framework import routers
from django.urls import include, path
from .api import New_FileViewSet
from . import api


router = routers.DefaultRouter()
router.register('newfile', New_FileViewSet, 'new_file')

urlpatterns = [
    path('', include(router.urls))
]
