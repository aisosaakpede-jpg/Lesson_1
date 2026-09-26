a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

original_a = a
original_b = b 

while b != 0:
    remainder = a % b
    a = b
    b = remainder
hcf = a
lcm = (original_a * original_b) // hcf
print("LCM =", lcm)