from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
import datetime


class AddHolidayForm(forms.Form):
    holiday_name = forms.CharField(label='holiday_name', max_length=50)
    holiday_date = forms.DateField(label='holiday_date')

    def clean_add_holiday_date(self):
        holiday_date = self.cleaned_data['holiday_date']
        return holiday_date


