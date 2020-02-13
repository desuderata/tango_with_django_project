from django.shortcuts import render
from django.http import HttpResponse

# views exists as a series of individual functions

def index(request):
    """ view 1: index

        Note:
            -\n doesnt work?

        Args:
            param1 (HttpRequest object): lives in the django.http module.
            named request due to convention.

        Returns:
            A HttpResponse object. Takes a string parameter representing the
            content of the page we wish to send to the client requesting the
            view.
            Shows text with hyperlink to about


    """
    return HttpResponse('<a href="/rango/about/">About</a>\nRango says hey there partner!')

def about(request):
    """ view 2: about

        Returns:
            A HttpResponse object to show text with hyperlink back to index.
    """
    return HttpResponse('<a href="/rango/">Index</a>\nRango says here is the about page')
