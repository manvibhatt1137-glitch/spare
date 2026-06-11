class Dog:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("bark")
class Cat:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("meow")
class Cow:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("moo")
    
d1 = Dog("labrador")
c1 = Cat("siamese")
co1 = Cow("mini cow")
for y in (d1,c1,co1):
    y.speak()