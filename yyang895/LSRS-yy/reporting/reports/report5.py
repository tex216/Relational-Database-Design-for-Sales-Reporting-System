from reporting.repository.sqlhelper import SqlHelper
from django.shortcuts import render
from django.http import JsonResponse
from reporting.forms import Report5SelectYearAndMonthForm
import calendar


def get_report_5(request):
    message = ""
    status = "success"

    if request.method == "GET":
        obj = SqlHelper()
        year_list = obj.get_year_list()
        obj.close()

        if len(year_list) == 0:
            status = "failed"
            message = "There is not year data."

        context = {
            'year_list': year_list,
            'message': message,
            'status': status
        }

        return render(request, 'reporting/report5_get_year_list.html', context)
    elif request.method == 'POST':

        form = Report5SelectYearAndMonthForm(request.POST)

        if form.is_valid():
            year_list = request.POST.get('year_list')
            month_list = request.POST.get('month_list')

            obj = SqlHelper()
            report5 = obj.get_report5(year_list, month_list)
            obj.close()

            message = year_list + ' ' + calendar.month_name[int(month_list)] + ' report'
            context = {
                'report5': report5,
                'message': message,
                'status': status
            }

            return render(request, 'reporting/report5_state_with_highest_volume.html', context)


def get_month_list(request):
    if request.method == 'GET':
        selected_year = request.GET.get('selected_year')
        obj = SqlHelper()
        month_list = obj.get_month_list(selected_year)
        obj.close()
        return JsonResponse(month_list, safe=False)
