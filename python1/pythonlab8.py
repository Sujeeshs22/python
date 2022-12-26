# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

num = random.randrange(1, 9)
number = int(input("gusees the number: "))
if (number > num):
    print("the number is too high")
elif (number < num):
    print('the number is too low')
elif (number == num):
    print("the number is right")
