from django.views import generic
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from reporting.forms import Report3SelectStateForm
from reporting.repository.sqlhelper import SqlHelper


def store_revenue(request):
    message = ""
    status = "success"

    if request.method == "GET":
        obj = SqlHelper()
        state_list = obj.get_state_list()
        obj.close()

        if len(state_list) == 0:
            status = "failed"
            message = "There is not GeoData."

        context = {
            'state_list': state_list,
            'message': message,
            'status': status,
            'report3': []
        }

        return render(request, 'reporting/report3_store_revenue_get_state.html', context)
    elif request.method == "POST":

        form = Report3SelectStateForm(request.POST)
        print ("touch post")
        if form.is_valid():
            state_location = request.POST.get('city_state_location')
            print(state_location)
            try:
                obj = SqlHelper()
                report3 = obj.report3_store_revenue_by_year_by_state(state_location)

                print(report3)
                obj.close()
                context = {
                    'report3': report3,
                    'state_list': [],
                    'message': message,
                    'status': status,
                }


                return render(request, 'reporting/report3_store_revenue.html', context)

            except Exception as e:
                message = "Exception {0} happens when selecting {1}. " \
                          "please refresh page".format(str(e), state_location)
                status = "failed"
                context = {
                    'state_list': [],
                    'message': message,
                    'status': status
                }
            return render(request, 'reporting/report3_store_revenue_get_state.html', context)
        else:
            obj = SqlHelper()
            state_list = obj.get_state_list()
            obj.close()

            message = "The submitted form is invalid, Please try again!"
            status = "failed"

            context = {
                'state_list': state_list,
                'message': message,
                'status': status
            }

            return render(request, 'reporting/report3_store_revenue_get_state.html', context)