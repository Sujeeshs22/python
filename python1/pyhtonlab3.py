# write a program that prints out all the elements of the list that are less than 5.
# Take this list

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


a = [1, 1, 1, 2, 3, 5, 8, 13, 21, 4, 55, 89]
result = []
for x in a:
    if (x < 5):
        result.append(x)
        print(result)
