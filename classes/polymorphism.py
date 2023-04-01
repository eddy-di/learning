from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control): # this is an instance of polymorphism, it allows to write cleaner code and not reqrite the whole chunks of code or rename it 
    # also it is useful to work with different types of objects
    # good for readability and clean code kinda 
    control.draw()

ddl = DropDownList()
draw(ddl)
txt = TextBox()
draw(txt)