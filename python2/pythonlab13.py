# Write a Python program to concatenate following dictionaries to create a new one.

# 	dic1={1:10, 2:20}
# 	dic2={3:30, 4:40}
# 	dic3={5:50,6:60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dict = {}
for x in dic1, dic2, dic3:
    dict.update(x)
    print(dict)


print(dict.values())
