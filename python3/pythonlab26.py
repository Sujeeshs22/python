# Write a Python program to append text to a file and display the text.


with open("text.txt", "a") as f:
    f.write("this is a text example")
    text = open("text.txt", "r")
    print(text.read())
