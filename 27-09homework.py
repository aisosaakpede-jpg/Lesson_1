# 2 digit prime numbers
# range is 10 to 99
#therefore for i in range(10,100?)
# apply guy-i-can't-spell's sieve
# trial and error :)

limit = 99
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
for number in range(11, limit + 1):
    if prime[number]:
        print(number, end=" ")
