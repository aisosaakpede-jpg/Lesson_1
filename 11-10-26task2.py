numbers = [4,1,2,1,2]
result = 0
for number in numbers:
    result = result^ number
    print("Correct numbers: ", number, "| Running XOR: ", result)
print("Number that occurs once: ", result)