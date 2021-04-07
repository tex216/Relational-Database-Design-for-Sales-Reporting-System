from django.views import generic
from reporting.repository.sqlhelperteng import SqlHelper


class GetReport(generic.ListView):
    template_name = "reporting/report1_category.html"
    context_object_name = "report1"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report1()
        obj.close()
        return report_res
