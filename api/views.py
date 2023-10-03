from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello World")