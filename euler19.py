week_day = 0
first_sundays = 0


for year in range(1900,2001):
    #print(year)
    for month in range(12):
        #print(month)
        for day in range(31):
            
            schaltjahr_flag = 28
            if year % 4 == 0:
                schaltjahr_flag = 29
                if year % 100 == 0 and year % 400 != 0:
                    schaltjahr_flag = 28
            if month == 1 and schaltjahr_flag == day:
                break
            if month == 3 and day == 30 or month == 5 and day == 30 or month == 8 and day == 30 or month == 10 and day == 30:
                break
            week_day += 1 
            if week_day == 7:
                week_day = 0
            if year > 1900 and day == 0 and week_day == 6:
                first_sundays += 1
            print(year, month + 1, day + 1)
print(first_sundays)