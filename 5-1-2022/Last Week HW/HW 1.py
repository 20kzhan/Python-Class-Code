def dayOfYear(date):
    nonleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]      # create nonleap year days and leap year days lists
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 2019-01-09
    # [2019, 01, 09]
    year = date.split('-')[0]       # extract year, month, day from date
    year = int(year)
    
    month = date.split('-')[1]
    month= int(month)
    
    day = date.split('-')[2]
    day = int(day)
    
    if year % 4 == 0 and year % 100 != 0:       # judge if a year is leap year and calculate the days accordingly
        days = sum(leap[:month]) + day - leap[month-1]
    elif year % 100 == 0 and year%400 != 0:
        days = sum(nonleap[:month]) + day - nonleap[month-1]
    elif year % 400 ==0:
        days = sum(leap[:month]) + day - leap[month-1]
    else:
        days = sum(nonleap[:month]) + day - nonleap[month-1]
    
    return days


print(dayOfYear("2019-01-09"))
