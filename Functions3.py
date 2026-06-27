def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
calculate = input("what do you want to do?(add/subtract/multiply/divide): ")

if calculate == "add":
    print(add(num1,num2))
elif calculate == "subtract":
    print(subtract(num1,num2))
elif calculate == "multiply":
    print(mul(num1,num2))
elif calculate == "divide":
    print(div(num1,num2))
else:
    print("Invalid")
