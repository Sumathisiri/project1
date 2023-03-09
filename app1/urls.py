from app1.views import *
from django.urls import path
app_name='Hello'

urlpatterns=[
    path('siri/',siri,name='siri'),
    path('siri2/',siri2,name='siri2'),
]