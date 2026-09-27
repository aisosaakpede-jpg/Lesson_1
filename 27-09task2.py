limit = int(input("Enter the limit: "))
prime = [True] * (limit + 1)
prime[0] = False
if limit >= 1:
    prime[1] = False
p = 2
while p * p <= limit:
    if prime[p] == True:
        for i in range(p*p,limit+1,p):
            prime[i] = False
    p = p +1
print("Prime numbers are: ")
for number in range(2, limit + 1):
    if prime[number]:
        print(number, end=" ")
