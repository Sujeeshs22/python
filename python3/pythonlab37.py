# Write a Python program to combine each line from first file with the corresponding line in second file.


with open("test.txt", "r") as f, open("test.txt", 'r')as g:
    for x, y in zip(f, g):
        print(x+y)
