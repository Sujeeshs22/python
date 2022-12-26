# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def num(n):
    if n < 1:
        return 0
    else:
        return n + num(n - 2)


print(num(7))
print(num(10))
