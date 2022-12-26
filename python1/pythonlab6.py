# Ask the user for a string and print out whether this string is a palindrome or not


txt = str(input("enter the text: "))
result = ""
for x in txt:
    result = x+result

if (txt == result):
    print("palindrome")
else:
    print("not palidrome")
