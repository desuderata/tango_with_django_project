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
    # return HttpResponse('<a href="/rango/about/">About</a>\nRango says hey there partner!')

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    """ view 2: about

        Returns:
            A HttpResponse object to show text with hyperlink back to index.
    """
    return HttpResponse('<a href="/rango/">Index</a>\nRango says here is the about page')
