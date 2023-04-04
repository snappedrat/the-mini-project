from django.contrib import admin
from django.urls import path, include
from .views import *
from django.urls import re_path as url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('ocr', ocr),
    path('camera', OCR, name='OCR')
]

# urlpatterns += staticfiles_urlpatterns()