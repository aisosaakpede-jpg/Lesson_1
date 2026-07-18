#Operations on Lists
fruits = ["Watermelon","Blackberry","Strawberry","rasberry","Banana"]

print(fruits)
fruits.append("Mango")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.insert(1,"Coconut")
print(fruits)
fruits.pop()
print(fruits)
print(fruits[0])
print(fruits[-1])
fruits[0] = "Random fruit"
print(fruits)
for i in fruits:
    print(i)