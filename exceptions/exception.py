# example when user enters not correct input
try:
    age = int(input("Age: "))
except ValueError:
    print("You did not enter a valid age.")
else:
    print("No exceptions were encountered.")
print("Going on smoothly")