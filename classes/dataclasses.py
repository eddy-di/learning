# it is possible to create classes to work with data and compare it using the magic methods __init__ and __eq__ 
# but there is a better way of working with data and that is namedtuples

from collections import namedtuple
# importing from collections namedtuple allows to worki with data and not create other classes and methods to 
# compare data of objects. Also you cannot add new value to existing objects, like making x from 1 to 10 is not possible

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)