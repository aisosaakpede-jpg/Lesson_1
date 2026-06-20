#Write a Python program to take a number as input from the user and check whether it is a prime number or not.

num = int(input("Enter number: "))
prime = True

if num < 2:
    prime = False

for i in range(2,num):
    if num % i == 0:
        prime = False
        break

if prime:
    print(num, "is a prime number") 
else:
    print(num, "is not a prime number")