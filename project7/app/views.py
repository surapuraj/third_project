from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':12}
    return render(request,'conditions.html',d)
    
