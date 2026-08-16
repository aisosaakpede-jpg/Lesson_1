def fibonacci(choice):
    a = 0
    b = 1
    for i in range(choice):
        print(a)
        next_num = a+b
        a = b
        b = next_num
x = int(input("Enter n: "))
fibonacci(x)