items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# line 7 has a map function + lambda in use (kinda noisy with all parantheses and etc)
# prices = list(map(lambda item: item[1], items))
# line 9 is similar to line 7 and uses list comprehension but cleaner 
prices = [item[1] for item in items]

# line 12 has a filter function + lambda in use (kinda noisy with all parantheses and etc)
# filtered = list(filter(lambda item: item[1] >= 10, items))
# line 14 is similar to line 12 and uses list comprehension but cleaner 
filtered = [item for item in items if item[1] >= 10]

print(prices)
print(filtered)