from django.views import generic
from reporting.models import HOLIDAY


class HolidayList(generic.ListView):
    context_object_name = 'holidayList'
    template_name = "reporting/holiday_list.html"

    def get_queryset(self):
        return HOLIDAY.objects.raw('SELECT * FROM holiday')

