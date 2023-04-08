items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# filtered = []
# for item in items:
    # filtered.append(item[1] >= 10)
# here's another code that filters with created function, 
# but gives boolean values as an output

filtered = list(filter(lambda item: item[1] >= 10, items))
# this version from video lesson, and uses lambda function
# in use to filter from the main list
print(filtered)