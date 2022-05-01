import datetime

def dayOfTheWeek(day, month, year):
    date = []
    date.append(str(day))
    date.append(str(month))
    date.append(str(year))
    # [day, month, year]
    
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = datetime.datetime.strptime("-".join(date), '%d-%m-%Y').weekday()
    # "day-month-year"
    # "2019-12-01"
    return day_name[day]
