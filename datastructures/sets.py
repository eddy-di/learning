# important to understand that sets are not indexed and are considered as unordered collection of items
# you will have a mistake in line 12 TypeError: 'set' object is not subscriptable
numbers = [1, 1, 2, 2, 3, 4,]
first = set(numbers)
second = {1, 3, 5}

print(first | second) # union - all items that are in both sets {1, 2, 3, 4, 5}
print(first & second) # intersection gets items that are in both sets and are similar {1, 3}
print(first - second) # difference - gets items that are in one of the sets and that are not interseting with second one {2, 4}
print(first ^ second) # symetric - gets items from both sets and not the intersecting ones {2, 4, 5}

# print(first[0])