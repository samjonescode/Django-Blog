from django.shortcuts import render
from django.http import HttpResponse

def GlobalHome(request):
    return HttpResponse("<h1> Welcome to the page, view the blog at /blog </h1>")
    