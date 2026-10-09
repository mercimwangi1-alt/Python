#behavihors---method,,,object and class has same things---class a two member,,variable//method
#class is a blueprint-
#in function,,varialbe to carry diff value pass them as parameters--def init used to help pass variable to parameters
class Student:
#variables of a class
    def __init__(self,name,age,gender,course):
        self.name=name
        self.age=age
        self.gender=gender
        self.course=course

    def study(self):
       print("Student is Studying")
    def sing(self):
       print("She is Singing")
stud1=Student("James",22,"M","MIT")
print(stud1.name)
stud1.study()
stud2=Student("Mary",40,"F", "software dev")
print(stud2.name)
stud2.sing()
stud3=Student("Jim",19,"F", "WEB")
print(stud3.name)
stud3.study()
#object,created as a variable
