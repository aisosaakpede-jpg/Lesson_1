number = 10
print("Original number: ", number)
print("Original binary: ", bin(number))
position = 0
mask = 1 << position
set_result = number | mask
print("After setting bit: ",position,":",set_result)
print("Binary after setting: ", bin(set_result))
position = 1
mask = 1 << position
zero_result = set_result & ~mask
print("After clearing bit: ",position,":",zero_result)
print("Binary after clearing: ", bin(zero_result))
n = int(input("Enter a non-negative number: "))
if n >0 and (n & (n-1)== 0): 
    print(n, "Is a power of 2")
else:
    print(n, "is not a power of 2")