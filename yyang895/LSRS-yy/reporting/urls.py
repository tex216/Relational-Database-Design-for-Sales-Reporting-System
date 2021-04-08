from django.urls import path
from reporting import views
from reporting.maintenances import holiday
from reporting.maintenances import population
from reporting.reports import report5, report7, report8, report9

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('population/', population.city_population_load, name='population'),
    path('population/get_city_list/', population.get_city_list, name='population_get_city_list'),
    path('population/get_city_population/', population.get_city_population, name='population_get_city_population'),
]

urlpatterns += [
    path('holiday/', holiday.HolidayList.as_view(), name='holiday'),
    path('holiday/add_holiday/', holiday.add_new_holiday, name='add_holiday')
]

urlpatterns += [
    path('report5_get_month_list/', report5.get_month_list, name='report5_get_month_list'),
    path('report5_state_with_highest_volume/', report5.get_report_5, name='report5_state_with_highest_volume'),
]

urlpatterns += [
    path("report7_childcare_sales_volume/", report7.GetReport.as_view(), name="report7_childcare_sales_volume")
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