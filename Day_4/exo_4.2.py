import random

names_string = input('Enter names: ')
names = names_string.split(', ')

random.shuffle(names)
print(f'{names[0]} is going to buy the meal today!')