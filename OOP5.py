#Create a program to introduce your robot using OOPs concepts.

class Robot:
    tool = "Robots: "
    def __init__(self,name,model,size,job):
        self.name = name
        self.model = model
        self.size = size
        self.job = job
    def intro(self):
        print("Good day, my name is ",self.name)
        print("My model is ",self.model)
        print("My size is ", self.size)
        print("And my job is ",self.job)

r1 = Robot("A5ZR","Articulated arms","5 meters","welding and material handling")
r2 = Robot("BeiBei","Humanoid","1.6 meters","being a waitress")
r3 = Robot("R2#4","SCARA","4 meters","industrial assembly of devices")

print(Robot.tool)
r1.intro()
print("")
r2.intro()
print("")
r3.intro()



