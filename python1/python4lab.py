# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.


num = int(input("enter the number: "))
result = []
for i in range(1, num+1):
    if (num % i == 0):
        result.append(i)
        print(result)
