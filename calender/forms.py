from django import forms

class GregorianDateForm(forms.Form):
    g_year = forms.IntegerField(label="Gregorian Year")
    g_month = forms.IntegerField(label="Gregorian Month")
    g_day = forms.IntegerField(label="Gregorian Day")
