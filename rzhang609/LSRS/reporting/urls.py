from django.urls import path
from reporting import views
from reporting.maintenances import holiday
from reporting.maintenances import population

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('holiday/', holiday.HolidayList.as_view(), name='holiday')
]

urlpatterns += [
    path('holiday/add_holiday/', holiday.add_new_holiday, name='add_holiday')
]

urlpatterns += [
    path('population/', population.city_population_load, name='population'),
    path('population/get_city_list/', population.get_city_list, name='population_get_city_list'),
    path('population/get_city_population/', population.get_city_population, name='population_get_city_population'),
]