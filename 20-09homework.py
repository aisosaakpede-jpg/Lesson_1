#Binary to decimal
#binary: 00000000 <- parts
#decimal: 128,64,32,16,8,4,2,1
# while loop probably
# convert binary variable to list
# check if number is 8 digits

binary = input("Enter 8 digit binary number: ")

original = int(binary)
binary = list(binary)
decimal = [128, 64, 32, 16, 8, 4, 2, 1]
store = 0
for i in range(8):
    
    if binary[i] == "1":
        store += int(decimal[i])
    else:
        continue
print("binary number ",str(original), " is decimal number",store)


