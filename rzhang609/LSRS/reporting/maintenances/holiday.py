from django.views import generic
from django import forms
from reporting.models import HOLIDAY


class HolidayList(generic.ListView):
    context_object_name = 'holidayList'
    template_name = "reporting/holiday_list.html"

    def get_queryset(self):
        return HOLIDAY.objects.raw('SELECT Name, Date FROM holiday')


class HolidayInput(forms.Form):
    holiday_name = forms.CharField(label='holiday_name', max_length=50)


