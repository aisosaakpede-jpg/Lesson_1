number = int(input("Enter a non-negative number"))
if number < 0:
    print("Please enter a non-negative number: ")
elif number == 0:
    print("there is no set bit in 0")
else: 
    print("Number: ", number)
    print("Binary: ", bin(number))
    for position in range(5):
        mask = 1 << position
        print("Bit position: ", position)
        print("Mask in decimal: ", mask)
        print("Mask in binary: ", bin(mask))
        if number & mask:
            print("Bit status: ON")
        else:
            print("Bit status: OFF")