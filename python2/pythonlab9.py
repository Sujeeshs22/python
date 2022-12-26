# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.3

import random

list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(list)
print(''.join(list))
