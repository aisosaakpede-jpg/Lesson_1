
class Student:
    grade = 10
    name = "Sasha"
    def message(self):
        
        print("I am a student named ",Student.name," and I am in grade ",Student.grade)
s1 = Student()
s1.message()