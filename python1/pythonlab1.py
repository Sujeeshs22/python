from datetime import date

# Write a program that asks the user to enter their name and their age.
# Print out a message that greets them and that tells them the year that they will turn 100 years old.


name = input("enter  name: ")
age = int(input("enter  age: "))
result = date.today()
print("hellow " + name + " you will turn 100yr in the year", (result.year-age)+100)
