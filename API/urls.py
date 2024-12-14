from django.contrib import admin
from django.urls import path, include
from API.views import *

urlpatterns = [
    path('', main, name='API_main'),
    path('get/<int:id>/', get, name='API_get'),
    path('post/', post, name='API_post'),
    path('delete/<int:id>/', delete, name='API_delete'),
    path('put/<int:id>/', put, name='API_put'),
]