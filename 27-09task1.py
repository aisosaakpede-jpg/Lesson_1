from math import sqrt
number = int(input("enter your number: "))
is_prime = True
if number < 2:
    is_prime = False
else: 
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")