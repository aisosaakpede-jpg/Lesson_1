#import modules
from abc import ABC, abstractmethod

#Make classes
class Instrument(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass
class Piano(Instrument):
    def __init__(self,name,kind):
        super().__init__(name)
        self.kind = kind
    def sound(self):
        print(self.name, " makes a plink sound")

class Trumpet(Instrument):
    def __init__(self,name,material):
        super().__init__(name)
        self.material = material
    def sound(self):
        print(self.name, " makes a honk sound")

class Xylophone(Instrument):
    def __init__(self,name,colour):
        super().__init__(name)
        self.colour = colour
    def sound(self):
        print(self.name, " makes a clink sound")

#object creation

p = Piano("piano","percussion")
t = Trumpet("trumpet","brass")
x = Xylophone("xylophone","brown")

#object action
p.sound()
print("A",p.name,"is a ",p.kind," instrument")
print()
t.sound()
print("A ",t.name,"is made of ",t.material)
print()
x.sound()
print("A ",x.name," is ",x.colour)
