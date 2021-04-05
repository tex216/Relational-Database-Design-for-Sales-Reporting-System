from django.shortcuts import render
from reporting.repository.sqlhelper import SqlHelper


def index(request):
    count_stores = 0
    count_stores_offering_food = 0
    count_stores_offering_childcare = 0
    count_products = 0
    count_distinct_advertising_campaigns = 0

    try:
        obj = SqlHelper()
        count_stores = obj.get_count_of_store()[0]['Count']
        count_stores_offering_food = obj.get_count_stores_offering_food()[0]['Count']
        count_stores_offering_childcare = obj.get_count_stores_offering_childcare()[0]['Count']
        count_products= obj.get_count_products()[0]['Count']
        count_distinct_advertising_campaigns = obj.get_count_distinct_advertising_campaigns()[0]['Count']
        obj.close()

        content = {
            'count_stores': count_stores,
            'count_stores_offering_food': count_stores_offering_food,
            'count_stores_offering_childcare': count_stores_offering_childcare,
            'count_products': count_products,
            'count_distinct_advertising_campaigns': count_distinct_advertising_campaigns,
            'status': "success"
        }
    except Exception as e:
        content = {
            'count_stores': count_stores,
            'count_stores_offering_food': count_stores_offering_food,
            'count_stores_offering_childcare': count_stores_offering_childcare,
            'count_products': count_products,
            'count_distinct_advertising_campaigns': count_distinct_advertising_campaigns,
            'status': "failed with exception {0}".format(str(e))
        }

    return render(request,'index.html', content)
