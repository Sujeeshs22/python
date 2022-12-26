# Write a Python program to count the number of lines in a text file.


def file(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
        return i+1


print("the number of lines in the file is ", file("test.txt"))
