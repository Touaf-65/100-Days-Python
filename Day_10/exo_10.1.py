def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

def days_in_month(month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(month_days[month-1])

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

is_leap(year)

days = days_in_month(month)












