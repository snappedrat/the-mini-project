from django.contrib import admin
from django.urls import path, include
from .views import *
from django.urls import re_path as url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('lipnet', lipnet),
    path('', index),
    path('camera', Home, name='lipnet')
]

urlpatterns += staticfiles_urlpatterns()