num = int(input("Enter number: "))
length = len(str(num))
store = 0

for char in str(num):
    store += int(char)**length
if store == num:
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")    
