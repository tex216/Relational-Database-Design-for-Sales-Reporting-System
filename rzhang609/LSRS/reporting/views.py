from django.shortcuts import render


def index(request):

    num_store = 0
    num_products = 0

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_store': num_store,'num_products':num_products},
    )
