from django.views import generic
from django.shortcuts import render
from reporting.forms import AddHolidayForm
from reporting.repository.sqlhelprzhang import SqlHelper


class HolidayList(generic.ListView):
    template_name = "reporting/holiday_list.html"
    context_object_name = 'holidayList'

    def get_queryset(self):
        obj = SqlHelper()
        holiday_list = obj.get_holiday_list()
        obj.close()
        return holiday_list


def add_new_holiday(request):
    if request.method == "POST":
        form = AddHolidayForm(request.POST)

        if form.is_valid():
            holiday_name= request.POST.get('holiday_name')
            holiday_date = request.POST.get('holiday_date')

            try:
                obj = SqlHelper()

                # check if holiday with the same day and same name existed or not
                is_holiday_existed = obj.check_if_holiday_existed(holiday_name, holiday_date)
                if is_holiday_existed > 0:
                    obj.close()
                    context = {
                        'message': "Holiday is existed with name: {0} and date: {1}".format(holiday_name, holiday_date),
                    }
                    return render(request, 'reporting/holiday_add_holiday.html', context)

                obj.add_holiday(holiday_name, holiday_date)
                obj.close()
                context = {
                    'message': "Holiday (name: {0} and date: {1}) is added".format(holiday_name, holiday_date),
                    'form': AddHolidayForm(),
                }
            except Exception as e:
                context = {
                    'message': "Exception {0} based on holiday name {1} "
                               "and holiday date {2}".format(str(e),holiday_name,  holiday_date)
                }
            return render(request, 'reporting/holiday_add_holiday.html', context)
    else:
        form = AddHolidayForm()

    context = {
        'form': form,
        'message': ""
    }

    return render(request, 'reporting/holiday_add_holiday.html', context)
