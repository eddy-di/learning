# values = []
# for x in range(5):
    # values.append(x * 2)

values = [x *2 for x in range(5)] # first 3 lines of code are similar to this line (list comprehension method)
values = {x *2 for x in range(5)} # changing this line into curly braces makes list into set (set comprehension method)
# to make comprehension method with ability to itirate over the items in dictionary line of code has to be like this
values = {x: x *2 for x in range(5)} # output = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
# but what will happen with output if the same line of code will be transformed into tuple
values = (x *2 for x in range(5)) # output = <generator object <genexpr> at 0x0000027D556A4110>
print(values)

# Python generators are objects that can be looped over similar to that of a list. 
# Unlike lists, lazy iterator contents are not stored in the memory. 
# The efficient way to iterate through large datasets is through the use of generators.

# To show an example of memory storage in big cases of data
from sys import getsizeof

values = (x *2 for x in range(100000))
print("gen:", getsizeof(values)) # output = gen: 208
values = [x *2 for x in range(100000)]
print("list:", getsizeof(values)) # output = list: 800984
