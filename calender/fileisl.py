from hijri_converter import convert

def convert_gregorian_to_islamic(g_year, g_month, g_day):  # it uses hijri_converter module to convert gregorian date to hijri 
    islamic_date = convert.Gregorian(g_year, g_month, g_day).to_hijri()
    islamic_day = islamic_date.day
    islamic_month_name = islamic_date.month
    islamic_year = islamic_date.year
    return islamic_day, islamic_month_name, islamic_year


def format_islamic_date(islamic_day, islamic_month_name, islamic_year): # to return a formatted date it takes the output of convert_gregorian function
    month_names = {
        1: 'Muharram',
        2: 'Safar',
        3: 'Rabi al-Awwal',
        4: 'Rabiʽ al-Thani',
        5: 'Jumada al-Awwal',
        6: 'Jumada al-Thani',
        7: 'Rajab',
        8: "Sha'ban",
        9: 'Ramadan',
        10: 'Shawwal',
        11: 'Dhu al-Qadah',
        12: 'Dhu al-Hajjah'
    }
    
    new_name = month_names[islamic_month_name]
    formatted_date = f"Today is the {islamic_day} of {new_name} month of the year {islamic_year}"
    return formatted_date
