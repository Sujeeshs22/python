# Write a Python program to generate all sublists of a list.


a = [1, 2, 3, 4]
lists = [[]]
for i in range(len(a) + 1):
    for j in range(i):
        lists.append(a[j: i])
        print(lists)
