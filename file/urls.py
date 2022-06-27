from django.urls import path
from .views import *


urlpatterns = [
    path('', simple_upload, name=''),
]

