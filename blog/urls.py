from rest_framework import routers
from .views import UserViewSet, EntryViewSet

from django.urls import path

from .import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('entries', EntryViewSet)

path('temp', views.temp, name='temp'),
