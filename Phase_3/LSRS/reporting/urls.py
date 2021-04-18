from django.urls import path
from reporting import views
from reporting.maintenances import holiday
from reporting.maintenances import population
from reporting.reports import report1, report2, report3, report4, report5, report6, report7, report8, report9

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('population/', population.city_population_load, name='population'),
    path('population/get_city_list/', population.get_city_list, name='population_get_city_list'),
    path('population/get_city_population/', population.get_city_population, name='population_get_city_population'),
    path('holiday/', holiday.HolidayList.as_view(), name='holiday'),
    path('holiday/add_holiday/', holiday.add_new_holiday, name='add_holiday')
]

urlpatterns += [
    path("report1_category/", report1.GetReport.as_view(), name="report1_category"),
    path("report2_actual_versus_predicted_revenue_for_couches_and_sofas/",
         report2.GetReport.as_view(), name="report2_actual_versus_predicted_revenue_for_couches_and_sofas"),
    path('report3_store_revenue_by_year_by_state/', report3.store_revenue,
         name='report3_store_revenue_by_year_by_state'),
    path("report4_outdoor_furniture_revenue/",  report4.GetReport.as_view(),name="report4_outdoor_furniture_revenue"),
    path('report5_get_month_list/', report5.get_month_list, name='report5_get_month_list'),
    path('report5_state_with_highest_volume/', report5.get_report_5, name='report5_state_with_highest_volume'),
    path('report6_revenue_by_population/', report6.GetReport6.as_view(), name='report6_revenue_by_population'),
    path("report7_childcare_sales_volume/", report7.GetReport.as_view(), name="report7_childcare_sales_volume"),
    path("report8_restaurant_impact_on_category_sales/",
         report8.GetReport.as_view(),name="report8_restaurant_impact_on_category_sales"),
    path("report9_advertising_campaign_analysis/",
         report9.GetReport.as_view(),name="report9_advertising_campaign_analysis")
]


