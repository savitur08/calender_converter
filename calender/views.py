from django.shortcuts import render
from .forms import GregorianDateForm 
from django.shortcuts import render
from hijri_converter import convert
from .fileisl import format_islamic_date,convert_gregorian_to_islamic
from .fileheb import gregorian_to_absdate,absdate_to_hebrew
from .fileind import gregorian_to_julian,fromjd


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


# The logic and source code
# Source code Copyright © by Ulrich and David Greve (2005)
def convert_gregorian_to_hebrew_view(request):
    if request.method == "POST":
        form = GregorianDateForm(request.POST)
        if form.is_valid():
            g_year = form.cleaned_data['g_year']
            g_month = form.cleaned_data['g_month']
            g_day = form.cleaned_data['g_day']
            
            absolute_date = gregorian_to_absdate(g_year, g_month, g_day) #function in files.py file it's job is to convert the gregorian dates to islamic hijri dates
            year,month,day= absdate_to_hebrew(absolute_date)   # to parse it into a string 
            
            return render(request, 'calender/resultheb.html', {'year': year,'month':month,'day':day})
    else:
        form = GregorianDateForm()
    return render(request, 'calender/convert.html', {'form': form})


#Converting to indian official date
def convert_gregorian_to_Indian_view(request):
    if request.method == "POST":
        form = GregorianDateForm(request.POST)
        if form.is_valid():
            g_year = form.cleaned_data['g_year']
            g_month = form.cleaned_data['g_month']
            g_day = form.cleaned_data['g_day']
            
            julian_date = gregorian_to_julian(g_year, g_month, g_day) #function in filesind.py file it's job is to convert the gregorian dates to julian day
            year,month,day= fromjd(julian_date)   # to parse it into a string 
            
            return render(request, 'calender/resultheb.html', {'year': year,'month':month,'day':day})
    else:
        form = GregorianDateForm()
    return render(request, 'calender/convert.html', {'form': form})