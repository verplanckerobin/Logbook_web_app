from django import forms
from .models import Aircraft, Airport, People, Log


class AircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        labels = {'aircraft_id':'Aircraft Registration', 'aircraft_type':'Aircraft Model', 'notes':'Remarks'}
        fields = ['aircraft_id', 'aircraft_type', 'notes']


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        labels = {'ICAO_code':'ICAO Code', 'IATA_code':'IATA Code', 'name':'Full Airport Name', 'country':'Country'}
        fields = ['ICAO_code', 'IATA_code', 'name', 'country']


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        labels = {'name':'Full Name', 'company_function':'Company Function', 'phone':'Phone', 'email':'Email', 'remarks':'Remarks'}
        fields = ['name', 'company_function', 'phone', 'email', 'remarks']


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        labels = {'date':'Date', 'departure':'Departure', 'block_out':'Time', 'arrival':'Arrival', 
        'block_in':'Time', 'aircraft':'Aircraft', 'pic':'PIC', 'landings':'Landing', 'take_off':'Take-off', 'remarks':'Remarks'}
        fields = ['date', 'departure', 'block_out', 'arrival', 'block_in', 'aircraft', 'pic', 'landings', 'take_off', 'remarks']