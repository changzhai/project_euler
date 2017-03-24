# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

startday = 365 % 7 + 1 #for monday
print(startday)

days = 365
sundays = 0

for year in range(1901,2001):
    for month in range(1,13):
        dayofweek = days%7+1
        print(str(year) + ', ' + str(month) + ', ' + str(dayofweek))
        if dayofweek == 7:
            sundays += 1
        if month in [1,3,5,7,8,10,12]:
            days += 31
        elif month in [4,6,9,11]:
            days += 30
        elif month == 2:
            if year % 400 == 0:
                days += 29
            elif year % 100 == 0:
                print(year)
                days += 28
            elif year % 4 == 0:
                days += 29
            else:
                days += 28
        
print(days)
print(sundays)