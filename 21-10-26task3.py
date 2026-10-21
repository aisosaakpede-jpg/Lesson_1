#sign detection
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
xor_result = a^b
print("Xor result: ", xor_result)
if xor_result < 0:
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")