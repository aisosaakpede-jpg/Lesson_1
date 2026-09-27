a = 3000
for num in range(1, a + 1):
    c = 0
    rev = 0
    temp = num
    for i in range(1, temp + 1):
        if num % i == 0:
            c = c+1
    temp = num
    while temp > 0:
        digit = temp% 10
        rev = rev * 10 + digit
        temp = temp // 10
print("Number: ",num,"Divisors: ",c,"Reverse: ",rev)