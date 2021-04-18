from django.views import generic
from reporting.repository.sqlhelper import SqlHelper


class GetReport(generic.ListView):
    template_name = "reporting/report2_actual_versus_predicted_revenue_for_couches_and_sofas.html"
    context_object_name = "report2"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report2()
        obj.close()
        return report_res