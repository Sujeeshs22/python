# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.


import random

upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowcase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "@#$%^&*.!"

combined = upcase+lowcase+numbers+symbols
length = 12

password = "".join(random.sample(combined, length))

print("the passwod is :", password)
