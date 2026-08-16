#details
student = ("Aisosa",14,"Year 9","Colyton Grammar School")

#subject sets
monday = {"English Lit","Maths","Physics","Chemistry","Biology","Computer Science"}
tuesday = {"French","Art","RPE","PE","PSHE","Maths"}
wednesday = {"PE","Geography","Physics","Computer Science","RPE","Maths"}
thursday = {"English Lang","Physics","Chemistry","Geography","French","Maths"}
friday ={"Art","French","Physics","English Lit","RPE","Chemistry"}

#main code
print("Tuple operations: ")
print()
print("Printing student details: ")
for i in range(len(student)):
    print(student[i])
print()
print("Printing student detail of index '2' ")
print(student[2])
print()
print("-----------------")
print()
print("Set operations")
#printing days
print("Monday: ")
print(monday)
print()

print("Tuesday")
print(tuesday)
print()

print("Wednesday")
print(wednesday)
print()

print("Thursday")
print(thursday)
print()

print("Friday")
print(friday)

print()
print("-----------------")
print()
#union
union = monday.union(tuesday)
print("A union of monday and tuesday subjects: ")
print(union)
print()
#intersect
inter = wednesday.intersection(friday)
print("An intersection of wednesday and friday subjects: ")
print(inter)
print()
#difference
dif = wednesday.difference(thursday)
print("A difference between wednesday and thursday subjects: ")
print(dif)
print()
#symmetric difference
sym_dif = tuesday.symmetric_difference(wednesday)
print("A symmetric difference between tuesday and wednesday subjects: ")
print(sym_dif)