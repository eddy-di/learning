class Animal:
    def eat(self):
        print("eat")

class Bird(Animal): # this is an example of one level inheritance
    def fly(self):
        print("fly")

class Chicken(Bird): # this is a two level inheritance, and in this case the method fly doesn't need to be executed
    pass # this line has to be writtten when creating classes because it needs some sort of command to execute. Leaving it empty is not good
# the main idea of the video 15 from Class topic is that when writing a code, you need to try to stick to one or two level inheritance models, and not make it more.