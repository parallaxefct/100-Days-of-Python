#prime number checker algorithm: simply check to see if any given number is a prime number
def prime_checker(number):
    #this filters 1 and below
    if number > 1:
        even = number % 2
        print(even)

n = int(input("Check this number: "))
prime_checker(number=n)
