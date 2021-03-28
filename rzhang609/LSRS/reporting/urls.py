from django.urls import path
from reporting import views
from reporting.maintenances import holiday

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('holiday/', holiday.HolidayList.as_view(), name='holiday')
]
