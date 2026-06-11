class Student:
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade
    
    def finals(self,grade):
        if grade < 3 :
            self.__grade = grade
        else:
            print("great!")
g1 = Student("ivi",5)
g2 = Student("liza",2)
print(g1.get_grade())
print(g2.get_grade())


