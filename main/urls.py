from django.urls import path
from django.urls.resolvers import URLPattern

from .import views


app_name = 'main'


urlpatterns = [
    path('', views.index, name='index'), ]
