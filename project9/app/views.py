from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def akhi(request):
    return HttpResponse('<marquee><h1>akhi is lazy girl</marquee></h1>')
