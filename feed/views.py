from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1>")
# Create your views here.
