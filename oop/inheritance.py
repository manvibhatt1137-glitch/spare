class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def new(self):
        print(self.name,self.age,self.grade)
class Grades(Student):
    pass
    
x = Grades('manvi',19, 3)
x.new()
