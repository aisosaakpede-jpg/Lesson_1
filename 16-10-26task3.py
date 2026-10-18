base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
if exponent < 0:
    print("Please enter a non-negative number")
else:
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = result * base
        base = base * base
        exponent = exponent >> 1
    print("Result: ",result)