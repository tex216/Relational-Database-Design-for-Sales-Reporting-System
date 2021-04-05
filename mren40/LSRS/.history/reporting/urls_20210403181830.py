from django.urls import path
from reporting import views
from reporting.maintenances import holiday
from reporting.maintenances import population
from reporting.reports import report8
from reporting.reports import report9

urlpatterns = [path("", views.index, name="index")]

urlpatterns += [path("holiday/", holiday.HolidayList.as_view(), name="holiday")]

urlpatterns += [path("holiday/add_holiday/", holiday.add_new_holiday, name="add_holiday")]

urlpatterns += [
    path("population/", population.city_population_load, name="population"),
    path("population/get_city_list/", population.get_city_list, name="population_get_city_list"),
    path("population/get_city_population/", population.get_city_population, name="population_get_city_population"),
]

urlpatterns += [
    path(
        "report8_restaurant_impact_on_category_sales/",
        report8.GetReport.as_view(),
        name="report8_restaurant_impact_on_category_sales",
    )
]

urlpatterns += [
    path(
        "report9_advertising_campaign_analysis/",
        report9.GetReport.as_view(),
        name="report9_advertising_campaign_analysis",
    )
]
