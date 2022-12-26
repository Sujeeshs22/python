# Write a Python program to get week number from 16/06/2015

from datetime import date, datetime


dat = date(2015, 6, 16)
print("the week number is :", dat.strftime("%W"))
print(datetime.today().strftime("%W"))
print(dat)
