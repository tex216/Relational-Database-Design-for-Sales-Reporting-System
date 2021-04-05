from django.views import generic
from django.shortcuts import render
from reporting.repository.sqlhelper import SqlHelper


class Report8(generic.ListView):
    template_name = "reporting/report8_restaurant_impact_on_category_sales.html"
    context_object_name = "holidayList"

    def get_queryset(self):
        obj = SqlHelper()
        holiday_list = obj.get_holiday_list()
        obj.close()
        return holiday_list
