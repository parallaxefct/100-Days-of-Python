#prime number checker algorithm: simply check to see if any given number is a prime number
def prime_checker(number):
    if number > 1:
        for index in range(2, number):
            if number % index:
                print('It\'s not a prime number.')
            else:
                print('It\'s a prime number.')



n = int(input("Check this number: "))
prime_checker(number=n)
