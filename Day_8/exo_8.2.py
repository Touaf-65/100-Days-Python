def primeCheck(n):
    is_prime = True
    for i in range(2,n-1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print('It\'s a prime number')
    else:
        print('It\'s not a prime number')

number = int(input('Enter a number: '))
primeCheck(number)