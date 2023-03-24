from rest_framework import routers
from django.urls import include, path
from .api import New_FileViewSet
from . import views


router = routers.DefaultRouter()
router.register('new_file', New_FileViewSet, 'new_file1')

urlpatterns = [
    path('', include(router.urls))
    # path('api-auth/', include(rest_framework.urls))
]
