items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# prices = []
# for item in items:
    # prices.append(item[1])
# in lines 7-9 there is function that help to map only 
# integers from tuples in original list
prices = list(map(lambda item: item[1], items))
# this line of code is similar to the code in lines 7-9 but it 
# uses lambda function and list built in func in Python
print(prices)