# * helps to unpack an object/value that has items in it which are iterable
numbers = [1, 2, 3] # output - [1, 2, 3]
print(*numbers) # if we want to make output like in line 4 need to add asterisk before argement numbers - print(*numbers)
print(1, 2, 3) # output - 1 2 3

# it works with range that is transformed into lists
values = list(range(7)) # output - [0, 1, 2, 3, 4, 5, 6]
values = [*range(5)] # output - [0, 1, 2, 3, 4]
values = [*range(5), *"Blah"] # output - [0, 1, 2, 3, 4, 'B', 'l', 'a', 'h'] strings are also unpacked when asterisk is added
print(values)

# it is also possible to combine several lists with unpacking operator
first = [1, 2]
second = [5, 7]
combined = [*first, "e", *second] # output - [1, 2, 'e', 5, 7]
print(combined)

# to unpack dictionaries we need to use two asterisks 
firstd = dict(x=1)
secondd = dict(x=15, y=4)
comb = {**firstd, **secondd, "z": 23} # output - {'x': 15, 'y': 4, 'z': 23}
# need to note that the last value will be given if the keys are same like in case of x in lines 19 and 20
print(comb)