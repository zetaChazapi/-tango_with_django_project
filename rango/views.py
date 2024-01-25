from django.http import HttpResponse
from django.shortcuts import render

# each view must return a HttpRespinse object - it takes a string representing the content of
# the page we wish to send to the client requesting the view


def about(request):
    about_context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, "rango/about.html", context=about_context_dict)


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    index_context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, "rango/index.html", context=index_context_dict)
