from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def chitti(request):
    return HttpResponse('<marquee><h1>chitti is a lazygirl</h1></marquee>')

