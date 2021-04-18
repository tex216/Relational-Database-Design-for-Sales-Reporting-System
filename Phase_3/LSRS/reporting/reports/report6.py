from django.views import generic
from reporting.repository.sqlhelper import SqlHelper


class GetReport6(generic.ListView):
    template_name = "reporting/report6_revenue_by_population.html"
    context_object_name = "report6"

    def get_queryset(self):
        obj = SqlHelper()
        report6_res = obj.report6_revenue_by_population()
        obj.close()
        return report6_res
