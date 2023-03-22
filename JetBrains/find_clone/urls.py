from rest_framework import routers
# from .api import New_FileViewSet
from . import views
from django.urls import path


# router = routers.DefaultRouter()
# router.register('api/new_file', New_FileViewSet, 'new_file')

urlpatterns = [# router.urls
    path('', views.index)
    # path('check_new_file', views.check_new_file_view)
]
