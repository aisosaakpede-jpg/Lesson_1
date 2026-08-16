#writing
file = open("shopping_list.txt","w")

file.write("___Fruit&Veg___\n")

file.write("carrot\n")
file.write("spinach\n")
file.write("tomatoes\n")
file.write("banana\n")
file.write("strawberry\n")
file.write("orange\n")

file.write("_____For_pancakes_and_coffee_____\n")

file.write("cream cheese\n")
file.write("egg\n")
file.write("flour\n")
file.write("demerara sugar\n")
file.write("coffee\n")
file.write("semi-skimmed milk\n")
file.close()
#read
print("_____Before update: ")
with open("shopping_list.txt","r") as file:
    blah = file.read()
print(blah)

#append
print("_____After update: ")
with open("shopping_list.txt","a") as file:
    thing = file.write("Baking soda\n")

with open("shopping_list.txt","r") as file:
    blah = file.read()
print(blah)
