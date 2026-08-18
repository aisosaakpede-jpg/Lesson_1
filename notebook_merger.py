#part1
import os 


with open("science_notes.txt","r") as file:
    see = file.read()
    print(see)
#part2

with open("maths_notes.txt","r") as file2:
    see2 = file2.readlines()
    print(see2)
    print(len(see2))

with open("thing.txt","w") as file3:
    file3.write(see)
    file3.write("\n")
    file3.write(str(see2))

if os.path.exists("thing.txt"):
    print("File exists")
    os.remove("thing.txt")
else:
    print("File doesn't exist")
