from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def akhila(request):
    return HttpResponse('<h1>my name is akhila</h1>')