import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
dice3 = ["blue", "yellow", "green", "pirates", "pirates", "pirates"]

rd1 = random.choice(dice1)
rd2 = random.choice(dice2)
rd3 = random.choice(dice3)

print(f"RED dice shows: {rd1}")
print(f"White dice shows: {rd2}")
print(f"Event dice shows: {rd3}")