year_limit = 90
age = int(input('Enter your age: '))

days = (year_limit - age) * 365
weeks = (year_limit - age) * 52
months = (year_limit - age) * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')