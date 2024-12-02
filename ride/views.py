from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def auto(request):
    return HttpResponse('<h1>Rides are availble here......!Any ride you want</h1>')

def bike(request):
    return HttpResponse('<h1>Enjoying the rides.....!</h1>')
