import random
import string

print(random.random()) # gives a floating number as a result
print(random.randint(1,6)) # gives integer as a result
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # picks one of the statement's from the list
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=2)) # picks given amount of choices "k=?" of the statement's from the list
print(random.choices("abcdefghijklmno", k=4)) # picks given amount of choices "k=?" of the statement's from the string making a list as an output
print("".join(random.choices("abcdefghi", k=8))) # picks given amount of choices "k=?" of the statement's from the string
print("".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))) # picks given amount of choices "k=?" from string.ascii_letters, digits and punctuation
# line 10 code is not a good password generator, it can be easily broken in less time than it takes to go for a walk 
base = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(base) # shuffles the order in a random manner
print(base)