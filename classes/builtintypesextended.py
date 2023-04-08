class Text(str):
    def duplicate(self):
        return self + self

class TracableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)
# it is possible to extend the built-in functions like in this examples, where the the duplicate method was added to str built-in class/function

text = Text("Python")
print(text.duplicate())

list = TracableList()
list.append('1')