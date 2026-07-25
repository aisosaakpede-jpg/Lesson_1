class Parrot:
    species = "parrot"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self):
        print(self.name," is singing")
    def dance(self):
        print(self.name," is dancing")
p1 = Parrot("Rin",5)
p2 = Parrot("Polly",30)
print(Parrot.species)
print(p1.name)
print(p1.age)
p1.sing()
p1.dance()
p2.sing()
p2.dance()
print(p2.name)
print(p2.age)
