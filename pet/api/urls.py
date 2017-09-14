from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter


from .viewsets import DogViewSet, CatViewSet

router = DefaultRouter()
router.register('dog', DogViewSet)
router.register('cat', CatViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
