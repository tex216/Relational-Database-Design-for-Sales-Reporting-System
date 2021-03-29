from django.views import generic
from django import forms
from reporting.models import HOLIDAY
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
import datetime
from reporting.forms import AddHolidayForm
from django.shortcuts import render
from django.db import connection, transaction
import MySQLdb


class HolidayList(generic.ListView):
    context_object_name = 'holidayList'
    template_name = "reporting/holiday_list.html"

    def get_queryset(self):
        return HOLIDAY.objects.raw('SELECT Name, Date FROM holiday')


def add_new_holiday(request):
    if request.method == "POST":
        form = AddHolidayForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            holiday_date = request.POST.get('holiday_date')
            holiday_name= request.POST.get('holiday_name')

            db = MySQLdb.connect(user='root', db='cs6400', passwd='GatechOmsCS2021', host='127.0.0.1',  charset='utf8')
            cursor = connection.cursor()
            cursor.execute("insert into day (date) values(%s)", [holiday_date])
            cursor.execute("insert into holiday (date, name) values(%s, %s)", [holiday_date, holiday_name])
            db.close()
    else:
        form = AddHolidayForm()

    context = {
        'form': form,
    }

    return render(request, 'reporting/holiday_add_holiday.html', context)


