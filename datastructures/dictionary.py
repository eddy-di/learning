# point = {"x": 1, "y": 2}
point = dict(x=1, y=2) #line 1 and 2 are identical, depends on preferences of a programmer, but it seems that 2 line is cleaner
point ["x"] = 10 # assigning new value to existing key
point ["z"] = 30 # creating new key and item in dictionary {'x': 10, 'y': 2, 'z': 30}
# if you will try to look for nonexistent key it will give key error llike in this example print(point["a"])
# this problem can be solved with logical operators and if
if "a" in point:
    print(point["a"])
print(point.get("a", 0)) # to look up something also can be used get built-in function
del point["y"] # some items can be also dleeted, accessing through key result will be {'x': 10, 'z': 30}
print(point)
# it is possible to loop with dictionary items
for x in point: # x also you can write - key
    print(x) # result will be x and y the keys of items
# to get values and keys there are two methods
# 1st one
for key in point:
    print(key, point[key]) # x 10 z 30
# 2nd method with two versions of output
for x in point.items():
    print(x) # will return tuples ('x', 10) and ('z', 30)
# it can be unpacked in this manner
for key, value in point.items():
    print(key, value) # result will be similar to the one in line 17 and 18