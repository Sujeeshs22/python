# Write a Python program to get days between two dates. Go to the editor
# Exampe: days between 28/02/2000 and  28/02/2001


from datetime import date, timedelta

dat = date(2000, 2, 28)
dat2 = date(2001, 2, 28)
result = dat2-dat
print(result)
