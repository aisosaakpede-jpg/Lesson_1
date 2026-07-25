class Parrot:
    species = "parrot"
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Parrot("Rin",5)
p2 = Parrot("Polly",30)
print(Parrot.species)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

        