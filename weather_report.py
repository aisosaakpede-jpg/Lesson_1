#You will build a Python program called my-weather-reporter.py.
#  The program asks for a city name and today's temperature,
#  checks the temperature with if, if-else, and if-elif-else to print a weather report, then uses the datetime and calendar modules to display the current date,
#  time, and a full year calendar.


import datetime
import calendar

city_name = input("What is your city name?: ")
temp = int(input("What is today's temperature?: "))

if temp > 25:
    print("It is hot today.")
elif temp < 25 and temp > 15 :
    print("It is warm today")
else:
    print("It is cold today")

date = datetime.datetime.now()
print(date.date())

print(date.time())

years = date.year
print(calendar.calendar(years))