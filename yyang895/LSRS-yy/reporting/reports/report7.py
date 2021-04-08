from django.views import generic
from reporting.repository.sqlhelper import SqlHelper
from django.template.defaulttags import register
from django.template import Variable, VariableDoesNotExist


@register.filter
def hash(object, attr):
    pseudo_context = { 'object' : object }
    try:
        value = Variable('object.%s' % attr).resolve(pseudo_context)
    except VariableDoesNotExist:
        value = None

    if (isinstance(value, str)):
        return value
    else:
        return int(value)


class GetReport(generic.ListView):
    template_name = "reporting/report7_childcare_sales_volume.html"
    context_object_name = "report7"

    def get_queryset(self):
        obj = SqlHelper()
        report_res = obj.get_report7()
        print(report_res, 'qq')
        obj.close()
        return report_res

