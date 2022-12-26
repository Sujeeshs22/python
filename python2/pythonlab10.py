# Write a Python program to count the number of characters (character frequency) in a string.

from collections import Counter


text = input("enter the string")
string = Counter(text)
print(string)