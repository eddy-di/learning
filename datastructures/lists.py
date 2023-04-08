num = list(range(20))
first, *other, last = num #this is an example of (un)packing a list
print(num[::2])
print(num[::-1])
print(first, last)
print(other)