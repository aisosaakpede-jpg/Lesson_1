#In this assignment, students will build a Pet Care Dashboard using Python object-oriented programming. 
# They will create a parent Pet class and different child pet classes,
#  override methods, protect private health data using encapsulation, and update pet health safely with setter methods. 
# The program also uses a loop to show polymorphism in action across different pet objects.

#Objective: Pet dashboard
#steps:
#Step1: Parent pet class is Pet
#Step2: constructor includes attributes - 
#Step3: Child pet classes are dog, cat, fish and snake

class Pet:
    def __init__(self,pet_name,user_name,animal):
        self.pet_name = pet_name
        self.user_name = user_name
        self.animal = animal
    def set_health(self,health_status):
        self.approved = ["healthy","sick","injured"]
        if self.__health_status in self.approved:
            self.__health_status = health_status
        else:
            print("Invalid health info")
    def display(self):
        pass
class Dog(Pet):
    def __init__(self,pet_name,user_name,animal,health_status):
        super().__init__(pet_name,user_name,animal)
        self.__health_status = health_status
    def set_health(self,health_status):
        self.approved = ["healthy","sick","injured"]
        if self.__health_status in self.approved:
            self.__health_status = health_status
        else:
            print("Invalid health info")
    def condition(self):
        print(self.pet_name,"is ",self._Dog__health_status)

    def display(self):
        print("The ",self.animal," ",self.pet_name,", owned by ",self.user_name, " is registered here")
class Cat(Pet):
    def __init__(self,pet_name,user_name,animal,health_status):
        super().__init__(pet_name,user_name,animal)
        self.__health_status = health_status
    def set_health(self,health_status):
        self.approved = ["healthy","sick","injured"]
        if self.__health_status in self.approved:
            self.__health_status = health_status
        else:
            print("Invalid health info")
    def condition(self):
        print(self.pet_name,"is ",self._Cat__health_status)

    def display(self):
        print("The ",self.animal," ",self.pet_name,", owned by ",self.user_name, " is registered here")

class Fish(Pet):
    def __init__(self,pet_name,user_name,animal,health_status):
        super().__init__(pet_name,user_name,animal)
        self.__health_status = health_status
    def set_health(self,health_status):
        self.approved = ["healthy","sick","injured"]
        if self.__health_status in self.approved:
            self.__health_status = health_status
        else:
            print("Invalid health info")
    def condition(self):
        print(self.pet_name,"is ",self._Fish__health_status)

    def display(self):
        print("The ",self.animal," ",self.pet_name,", owned by ",self.user_name, " is registered here")

d = Dog("Tommy","Anna","dog","sick")
c = Cat("Lola","Silvie","cat","injured")
f = Fish("Max","Siddarth","fish","healthy")
print("---Displaying information and condition---")

d.display()
d.condition()
print("")
c.display()
c.condition()
print("")
f.display()
f.condition()
print("")
print("")
print("---before setter method---")
f.__health_status = "injured"
f.condition()
print("")
print("---after setter method---")
f.set_health("sick")
f.condition()



