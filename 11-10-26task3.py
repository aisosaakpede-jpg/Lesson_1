numbers = [2,4,7,9,4,2]
xor_result = 0
for number in numbers:
    xor_result = xor_result ^ number
print("XOR of the two unique numbers: ", xor_result)
mask = xor_result & -xor_result
print("Mask in decimal: ", mask)
print("Mask in binary: ", bin(mask))
first = 0
second = 0
for number in numbers:
    if number & mask:
        first = first ^ number
    else:
        second = second ^ number
print("First number that occurs once: ", first)
print("Second number that occurs once: ", second)