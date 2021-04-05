from django.views import generic
from reporting.repository.sqlhelper import SqlHelper


class GetReport(generic.ListView):
    template_name = "reporting/report8_restaurant_impact_on_category_sales.html"
    context_object_name = "report8"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report8()
        obj.close()
        return report_res
