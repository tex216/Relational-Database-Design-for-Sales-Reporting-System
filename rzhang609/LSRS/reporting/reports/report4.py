from django.views import generic
from reporting.repository.sqlhelper import SqlHelper


class GetReport(generic.ListView):
    template_name = "reporting/report4_outdoor_furniture_revenue.html"
    context_object_name = "report4"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report4()
        obj.close()
        return report_res
