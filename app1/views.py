from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def siri(request):
    return HttpResponse('<h1><marquee>srujanaaaa</marquee></h1>')
def siri2(request):
    return HttpResponse('<h2>hello....</h2>')
