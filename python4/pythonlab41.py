# Write a Python program to subtract five days from current date

from datetime import date, timedelta

today = date.today()
x = timedelta(5)
datnow = today-x
print(datnow)
