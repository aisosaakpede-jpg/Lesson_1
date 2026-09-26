num = int(input("Enter number: "))
reverse = 0
original = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")