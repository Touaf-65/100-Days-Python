bill = 0

pizza = input('Enter the type of pizza: ')
pep = input('Do you want pepperoni? : ')
cheese = input('Do you want extra cheese? : ')

if pizza == 'S':
    bill += 15
    if pep == 'y': bill += 2
elif pizza == 'M':
    bill += 20
    if pep == 'y': bill += 3
elif pizza == 'L':
    bill += 25
    if pep == 'y': bill += 3

if cheese == 'y': bill += 1

print(f'Your final bill is: ${bill}.')

