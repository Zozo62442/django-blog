from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Hello, blog!")