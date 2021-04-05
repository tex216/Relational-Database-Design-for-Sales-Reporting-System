from django import forms


class AddHolidayForm(forms.Form):
    holiday_name = forms.CharField(label='holiday_name', max_length=50)
    holiday_date = forms.DateField(label='holiday_date')

    def clean_add_holiday_date(self):
        holiday_name = self.cleaned_data["holiday_name"]
        holiday_date = self.cleaned_data['holiday_date']
        return holiday_name, holiday_date


class UpdateCityPopulationForm(forms.Form):
    city_state_location = forms.CharField(label='city_state_location', max_length=50)
    city_name = forms.CharField(label='city_name', max_length=50)
    city_population = forms.IntegerField(label='city_population')

    def clean_add_holiday_date(self):
        city_state_location = self.cleaned_data['city_state_location']
        city_name = self.cleaned_data['city_name']
        city_population = self.cleaned_data['city_population']
        return city_state_location, city_name, city_population
