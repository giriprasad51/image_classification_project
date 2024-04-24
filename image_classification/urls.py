# image_classification/urls.py

from django.urls import path
from .views import classification_image,get_class_name_view

urlpatterns = [
    path('upload/', classification_image, name='upload_image'),
    path('get_class_name/', get_class_name_view, name='get_class_name'),
]