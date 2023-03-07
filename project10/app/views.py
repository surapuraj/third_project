from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def akhila(request):
    return HttpResponse('<marquee><h1>akhila is a akhila</marquee></h1>')
