letters = ["a", "b", "c", "d"]

print(letters)
# Add
letters.append("e")
letters.insert(0, 1)
print(letters)

#Remove
letters.pop() # also can add index to specifically get rid of an item from list
letters.remove("c") # remove is used when you don't know the index
del letters [0:2] # removes items in range
letters.clear() #removes all items
print(letters)