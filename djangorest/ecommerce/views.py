from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("You are at Ecommerce Index Page.")

def about(request):
    return HttpResponse("Ecommerce About page.")