def power_of_two(n):
    return (n & (n-1)) == 0
def power_of_four(n):
    return (n & (n-1)) == 0 and n % 3 == 1
def power_of_eight(n):
    return (n & (n-1)) == 0 and n % 7 == 1

num = int(input("Enter a number:"))
if power_of_four(num):
    print(num, "is a power of 4")
else:
    print(num, "is not power of 4")
if power_of_eight(num):
    print(num, "is a power of 8")
else:
    print(num, "is not power of 8")