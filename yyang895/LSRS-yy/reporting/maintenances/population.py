from django.http import JsonResponse
from django.shortcuts import render
from reporting.forms import UpdateCityPopulationForm
from reporting.repository.sqlhelper import SqlHelper


def city_population_load(request):
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
            'status': status
        }

        return render(request, 'reporting/population_maintenance.html', context)
    elif request.method == "POST":

        form = UpdateCityPopulationForm(request.POST)

        if form.is_valid():
            state_location = request.POST.get('city_state_location')
            city_name= request.POST.get('city_name')
            city_population = request.POST.get('city_population')
            try:
                obj = SqlHelper()
                obj.update_city_population(state_location, city_name, city_population)
                state_list = obj.get_state_list()
                obj.close()
                message = "The population has been updated for state {0}, city {1} " \
                          "to population {2}".format(state_location,city_name, city_population)

                context = {
                    'state_list': state_list,
                    'message': message,
                    'status': status,
                }
            except Exception as e:
                message = "Exception {0} happens when update the population of  state {1}, city {2} to population {3}. " \
                          "please refresh page".format(str(e), state_location,city_name, city_population)
                status = "failed"
                context = {
                    'state_list': [],
                    'message': message,
                    'status': status
                }
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

        return render(request, 'reporting/population_maintenance.html', context)


def get_city_list(request):
    if request.method == 'GET':
        state_location = request.GET.get('city_state_location')
        obj = SqlHelper()
        city_list = obj.get_city_list(state_location)
        obj.close()
        return JsonResponse(city_list, safe=False)


def get_city_population(request):
    if request.method == 'GET':
        state_location = request.GET.get('city_state_location')
        city_name = request.GET.get('city_name')
        obj = SqlHelper()
        city_population = obj.get_city_population(state_location, city_name)
        obj.close()
        return JsonResponse(city_population, safe=False)
