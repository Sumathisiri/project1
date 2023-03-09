from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def srujana(request):
    return HttpResponse('<h2>sirii..</h2>')
def srujana2(request):
    return HttpResponse('<h1>how are you..</h1>')
