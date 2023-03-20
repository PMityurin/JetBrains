from rest_framework import routers
from .api import New_FileViewSet


router = routers.DefaultRouter()
router.register('api/new_file', New_FileViewSet, 'new_file')

urlpatterns = router.urls

