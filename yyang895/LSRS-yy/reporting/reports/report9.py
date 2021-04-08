from django.views import generic
from reporting.repository.sqlhelper import SqlHelper


class GetReport(generic.ListView):
    template_name = "reporting/report9_advertising_campaign_analysis.html"
    context_object_name = "report9"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report9()
        obj.close()
        return report_res
