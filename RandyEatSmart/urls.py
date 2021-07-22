from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'randy', RandyViewSet, basename="test")
router.register(r'robert', RobertViewSet, basename="test2")
# router.register(r'robert/<int:key>', RobertViewSet, basename = "test2")

urlpatterns = router.urls
