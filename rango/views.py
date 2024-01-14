from django.http import HttpResponse
from django.shortcuts import render

# each view must return a HttpRespinse object - it takes a string representing the content of
# the page we wish to send to the client requesting the view


def index(request):
    return HttpResponse("Rango says hey there partner!")
