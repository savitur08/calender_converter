from django.shortcuts import render
from .forms import GregorianDateForm 
from django.shortcuts import render
from hijri_converter import convert
from .file import format_islamic_date
from .file import convert_gregorian_to_islamic

#importing form and setting up the view 

def convert_gregorian_to_islamic_view(request):
    if request.method == "POST":
        form = GregorianDateForm(request.POST)
        if form.is_valid():
            g_year = form.cleaned_data['g_year']
            g_month = form.cleaned_data['g_month']
            g_day = form.cleaned_data['g_day']
            
            islamic_day, islamic_month_name, islamic_year = convert_gregorian_to_islamic(g_year, g_month, g_day) #function in files.py file it's job is to convert the gregorian dates to islamic hijri dates
            formatted_islamic_date = format_islamic_date(islamic_day, islamic_month_name, islamic_year)   # to parse it into a string 
            
            return render(request, 'calender/result.html', {'formatted_islamic_date': formatted_islamic_date})
    else:
        form = GregorianDateForm()
    return render(request, 'calender/convert.html', {'form': form})
