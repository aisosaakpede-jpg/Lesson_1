from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(self.name, " says Woof")
class Parrot(Animal):
    def __init__(self,name,colour):
        super().__init__(name)
        self.colour = colour
    def speak(self):
            print(self.name, " says Hello")
class Lion(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def speak(self):
            print(self.name, " says ROAR!!!!")
#object creation
d = Dog("Dog","Rottweiler")
p = Parrot("Parrot","Rainbow")
l = Lion("Lion",25)

#print
print(d.name)
print(d.breed)
d.speak()

print(p.name)
print(p.colour)
p.speak()

print(l.name)
print(l.age)
l.speak()