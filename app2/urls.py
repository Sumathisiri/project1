from app2.views import *
from django.urls import path
app_name='HAPPY'


urlpatterns=[
    path('srujana/',srujana,name='srujana'),
    path('srujana2/',srujana2,name='srujana2'),
]