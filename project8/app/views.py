from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def prabhas(request):
    return HttpResponse('<marquee><h1>prabhas is king</marquee></h1>')
