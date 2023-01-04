# use arrays only if you are dealing with large sequence of numbers (more than 10_000)
# and encounter a performance problems. For other cases use lists and tuples by default.
from array import array #importing array module

numbers = array("i", [1, 2, 3]) #defining array of type 
numbers.append(5)
numbers.remove(3)
print(numbers)