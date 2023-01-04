# 1 method of swapping variables
x = 10
y = 13

z = x
x = y
y = z
print("x", x)
print("y", y)

# 2 method is using tuples
x = 10
y = 33
x, y = y, x
print("x", x)
print("y", y)