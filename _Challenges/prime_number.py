#prime number checker algorithm: simply check to see if any given number is a prime number
def prime_checker(number):
    #this filters 1 and below
    if number > 1:
        if number % 2 == 0:
            print('It\'s not a prime number.')
        elif number % 3 == 0:
            print('It\'s not a prime number.')
        else:
            print('It\'s a prime number.')


n = int(input("Check this number: "))
prime_checker(number=n)
