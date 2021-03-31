from django.urls import reverse
from django.views import generic
from django import forms
from reporting.models import HOLIDAY
from reporting.forms import AddHolidayForm
from django.shortcuts import render
from django.db import connection, transaction


class HolidayList(generic.ListView):
    context_object_name = 'holidayList'
    template_name = "reporting/holiday_list.html"

    # need add auto increased id as primary key
    def get_queryset(self):
        return HOLIDAY.objects.raw("SELECT Name, Date FROM Holiday")


def add_new_holiday(request):
    from django.shortcuts import redirect

    if request.method == "POST":
        form = AddHolidayForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            holiday_date = request.POST.get('holiday_date')
            holiday_name= request.POST.get('holiday_name')

            cursor = connection.cursor()
            cursor.execute("INSERT INTO `DAY` (`Date`) SELECT %s FROM `DAY` "
                           "WHERE NOT EXISTS (SELECT 1 FROM `DAY` WHERE `Date` = %s) LIMIT 1;",
                           [holiday_date, holiday_date])
            cursor.execute("INSERT INTO HOLIDAY (`Date`, `Name`) "
                           "SELECT %s, %s "
                           "FROM HOLIDAY WHERE NOT EXISTS ("
                           "SELECT 1 FROM HOLIDAY WHERE `Date` = %s AND `Name` = %s)"
                           "LIMIT 1;", [holiday_date, holiday_name, holiday_date, holiday_name])
            cursor.close()

            return redirect("/reporting/holiday/")
            #url = reverse('holiday', kwargs={'holiday_add_status': "success"})
            #return HttpResponseRedirect(url)
    else:
        form = AddHolidayForm()

    context = {
        'form': form,
    }

    return render(request, 'reporting/holiday_add_holiday.html', context)