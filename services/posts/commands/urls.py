from django.urls import path, include
from rest_framework import routers
from .views import CommandViewSet

router = routers.DefaultRouter()
router.register("", CommandViewSet)

urlpatterns = [path("", include(router.urls))]
