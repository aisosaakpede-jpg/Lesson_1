def factorial(k):
    if k == 1:
        return 1
    else:
        return k*factorial(k-1)

ans = int(input("Enter num: "))
print(factorial(ans))