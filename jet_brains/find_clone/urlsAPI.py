from rest_framework import routers
from django.urls import include, path
from .api import ResultViewSet, New_FileViewSet
from . import api


router = routers.DefaultRouter()
router.register('result', ResultViewSet, 'result')
router.register('newfile', New_FileViewSet, 'new_file')
# router.register('newfile', All_infoViewSet, 'all_info')


urlpatterns = [
    path('', include(router.urls))
]
