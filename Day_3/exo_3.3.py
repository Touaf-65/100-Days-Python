year = int(input('Enter your year: '))

if year % 4 == 0 or year % 400 == 0:
    print('Leap year.')
else:
    print('Not Leap year.')