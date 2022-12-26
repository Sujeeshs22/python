# Write a Python program to sort a dictionary by key.
# 	color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}


for x in sorted(color_dict):
    print(x, color_dict[x])
