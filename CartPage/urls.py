from django.urls import path, re_path

from CartPage.views import *

urlpatterns = [
    path('', main, name='cartPage'),
]