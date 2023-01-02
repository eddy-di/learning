items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])
# in lines 7-9 there is function that help to map only 
# integers from tuples in original list
print(prices)