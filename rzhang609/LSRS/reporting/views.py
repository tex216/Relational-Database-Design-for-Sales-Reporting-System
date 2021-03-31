from django.shortcuts import render
from .models import STORE, CHILDCARE, CITY, PRODUCT, SELL,DAY, SALE
from .models import CATEGORY, ASSIGNED, HOLIDAY, DISCOUNT, ADVERTISIN_GCAMPAIGN, HOLD


def index(request):

    num_store = STORE.objects.all().count()
    num_products = PRODUCT.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_store': num_store,'num_products':num_products},
    )
