items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


items.sort(reverse=True, key=lambda item:item[1])
# Here the lambda function is used "key=lambda item:item[1]" and 
# it is used instead of creating new function like in previous version with def sort_item etc.
print(items)