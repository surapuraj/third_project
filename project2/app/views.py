from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sarala(request):
    return HttpResponse('<marquee><h1>sarala is a good girl</h1></marquee>')
