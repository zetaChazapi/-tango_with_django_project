from django.http import HttpResponse
from django.shortcuts import render

# each view must return a HttpRespinse object - it takes a string representing the content of
# the page we wish to send to the client requesting the view


def index(request):
    html_content = (
        '<a href="/rango/about/">About</a><br>Rango says Hey welcome to the Homepage!'
    )
    return HttpResponse(html_content)


def about(request):
    html_content = '<a href= "/rango/">Index</a><br>This is the About Page!'
    return HttpResponse(html_content)
