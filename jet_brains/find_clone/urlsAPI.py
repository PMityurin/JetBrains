from rest_framework import routers
from .api import New_FileViewSet
from . import views


router = routers.DefaultRouter()
router.register('new_file', New_FileViewSet, 'new_file555')

urlpatterns = router.urls