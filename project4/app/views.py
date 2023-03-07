from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dilip(request):
    return HttpResponse('<marquee><h1>dilip is a handsome hunk</h1></marquee>')