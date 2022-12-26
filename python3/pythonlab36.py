# Write a Python program to copy the contents of a file to another file .


with open("test.txt", 'r')as f, open("this.txt", 'a') as g:
    for x in f:
        g.write(x)
