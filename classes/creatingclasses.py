class Point: # naming of classes has to be under Pascal Naming Convention (this example could've been MyPoint or smt like that)
    def draw(self): # here naming is the standart all lowercase and underscore, because its a function
        print("draw")

point = Point()
print(type(point))
print(isinstance(point, Point)) # isinstance shows the boolean expression that checks if one of the types is in the given class
print(isinstance(point, int)) # this will show Falsy value due to the fact that point is not in integer class