letters = ["a", "b", "c", "2", "4", "e", "5", "8"]
print(letters.count("3")) # count gives number of occurences of an item in a list
if "3" in letters:
    print(letters.index("3")) # without if the result will give an error of not having such item in list
    