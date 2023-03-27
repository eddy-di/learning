class Animal:
    def __init__(self):
        print("Animal Consturctor")
        self.age = 1
    
    def eat(self):
        print("eat")

class Mammal(Animal): # in parantheses the Animal word means that the initial age and eat methods are inherited by this Mammal class
    def __init__(self): # it is possible to override base/parent class constructor method if the line with super().__init__() won't be added the Animal parent class constructor won't be working
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2
    
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(m.age)
print(m.weight)
