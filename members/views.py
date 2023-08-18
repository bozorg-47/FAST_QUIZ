from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("hello people ")

# Create your views here.
