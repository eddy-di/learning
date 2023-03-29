# 1 example a bad practise that has to be avoided
class Employee():
    def greet(self):
        print("Employee Greeting")

class Person():
    def greet(self):
        print("Person Greeting")

class Manager(Employee, Person): #here's and exmaple of multiple inheritance, where you can put as parameters in brackets other classes
    pass
# the bad part of such practice stems in that if there will be an object within class manager, the first stated parameter will be executed if greet method will be called
m = Manager()
m.greet() # the result of this code is "Employee Greeting" if it sees the greet function on first parameter Employee it executes it and stops looking, because of the linear logic
# such practice can lead to bugs when working in teams other programmers will change the place of parameters in class Manager, and the eventual result will be different than what others will be expecting
# Main thing to take is that you don't put similar methods in classes, and then put them together as multiple classes (parameters) in other classes



# a good example is as follows
class Flyer(): # lets imagine that this class performs action of flying
    pass

class Swimmer(): # lets imagine that this class performs action of swimming
    pass

class FlyingFish(Flyer, Swimmer): # this case is an example of two distinctively behaving classes incorporated into another class
    pass