class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Work(self):
        print(f"my dog,{self.name} runs very fast")

x = Dog("max",3)
print(x.name)
x.Work()