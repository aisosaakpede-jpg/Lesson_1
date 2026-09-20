num = int(input("Enter number: "))
og = num #original
num_of_digits = len(str(num))
sum_of_powers = 0

while num > 0: 
    digit = num % 10
    sum_of_powers = sum_of_powers + digit ** num_of_digits
    num = num // 10

if sum_of_powers == og:
    print(og, " is an Armstrong Number")
else:
    print(og, " is not an Armstrong Number")
