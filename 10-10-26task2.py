number = int(input("Enter a non-negative number: "))
if number < 0:
    print("Please enter a non-negative number: ")
elif number == 0:
    print("there is no set bit in 0")
else: 
    temp = numberposition = 0
    while (temp & 1) == 0:
        temp = temp>> 1
        position +=1
    print("Number: ", number)
    print("Binary: ", bin(number))
    print("First set it position: ", position)