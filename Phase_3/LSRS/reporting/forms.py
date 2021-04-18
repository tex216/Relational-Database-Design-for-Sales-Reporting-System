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


class Report3SelectStateForm(forms.Form):
    city_state_location = forms.CharField(label='city_state_location', max_length=50)

    def clean_select_state(self):
        city_state_location = self.cleaned_data['city_state_location']
        return city_state_location


class Report5SelectYearAndMonthForm(forms.Form):
    year_list = forms.CharField(label='year_list', max_length=50)
    month_list = forms.CharField(label='month_list', max_length=50)

    def clean_select_year_month(self):
        year_list = self.cleaned_data['year_list']
        month_list = self.cleaned_data['month_list']
        return year_list, month_list
