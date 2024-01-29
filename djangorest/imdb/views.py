from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("You are at imdb idex page.")

def about(request):
    return HttpResponse("Imdb About page.")