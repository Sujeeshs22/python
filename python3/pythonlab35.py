# Write a Python program to write a list to a file.


li = ["an", "is", "what", "it", "those"]


def writefile(fname):
    with open(fname, 'w') as file:
        for x in li:
            file.write(x)


print(writefile("test.txt"))
