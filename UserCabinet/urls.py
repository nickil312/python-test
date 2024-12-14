from django.contrib import admin
from django.urls import path, include
from UserCabinet.views import *


urlpatterns = [
    path('', main,name='userCab'),

]