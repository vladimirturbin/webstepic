from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse("Hello world")

# Create your views here.
