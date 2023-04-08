class Point: # Pascal Naming Convention
    def __init__(self, x, y): # self is referencing current object that you are working with and you don't need to supply a value to it when calling it, Python interpreter will do it automatically
    # def __init__ is called a magic method or constructor and is executed when we create a new object. In this case point object    
        self.x = x
        self.y = y

    
    def draw(self): # standart naming convention
        print(f"Point ({self.x}, {self.y})")

point = Point(4, 7)
print(point.x)
point.draw()

print(type(point))
print(isinstance(point, Point)) # isinstance shows the boolean expression that checks if one of the types is in the given class
print(isinstance(point, int)) # this will show Falsy value due to the fact that point is not in integer class