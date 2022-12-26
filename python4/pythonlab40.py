# 1. Write a Python script to display the
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week


from datetime import date, time

print('Current date and time:', date.today())
print('Current year:', date.today().year)
print('Month of year:', date.today().strftime("%B"))
print("Week number of the year :", date.today().strftime("%W"))
print("week day of the week:", date.today().strftime("%w"))
print("days of year :", date.today().strftime("%j"))
print("day of the month :", date.today().strftime("%d"))
print("day of the week:", date.today().strftime("%A"))
