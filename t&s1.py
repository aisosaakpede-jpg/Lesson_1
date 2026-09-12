n = int(input("Enter n: "))
total = 0

for i in range(1,n+1):
    total += i
print(i)

total = 0
for i in range(1,1000001):
    total += i
print(i)

n = 1000000
total = n* (n+1)//2
print(total)

n=5
total= 0
for i in range(1,n+1):
    for j in range(i):
        total += i
print(total)