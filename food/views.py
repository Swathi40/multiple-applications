from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def veg(request):
    return HttpResponse('<h1>veggies good for health......!</h1>')

def Nonveg(request):
    return render(request,'Nonveg.html')
