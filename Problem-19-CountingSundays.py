"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
""" -have function know what name of day was for specific date (input day, month, year)
    - build all dates from 1 jan 1901 to 31 dec 2000
    - for each of first months ask if it is sunday
"""
monthDays =[None,31,28,31,30,31,30,31,31,30,31,30,31]
dayNames = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def numberOfDaysInYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365

def numberOfDaysInMonth(month, year):
    if month == 2:
        if isLeapYear(year):
            return monthDays[2] + 1
        else:
            return monthDays[2]
    else:
        return monthDays[month]

def getDateName(day, month, year):
    #counts how many days from 1 jan 1900 to date
    #dividing that by 7 and getting remainder gets day name

    #figure out how many days between years
    daysBetweenYears = 0
    for y in xrange(1900, year):
        daysBetweenYears += numberOfDaysInYear(y)
    
    daysBetweenMonths = 0
    #figure out how many days from start of year to month
    for m in xrange(1,month):
        daysBetweenMonths += numberOfDaysInMonth(m, year) 

    daysFromPivotDate = day + daysBetweenYears + daysBetweenMonths
    print dayNames[daysFromPivotDate % 7]



