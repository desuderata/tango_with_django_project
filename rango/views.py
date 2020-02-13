from django.shortcuts import render
from django.http import HttpResponse

# views exists as a series of individual functions

def index(request):
    """ view 1: index

        Args:
            param1 (HttpRequest object): lives in the django.http module.
            named request due to convention.

        Returns:
            A HttpResponse object. Takes a string parameter representing the
            content of the page we wish to send to the client requesting the
            view


    """
    return HttpResponse("Rango says hey there partner!")
