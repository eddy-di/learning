# example when user enters not correct input
try:
    age = int(input("Age: "))
except ValueError as ex: # the ex part is considered as very technical, and may not be included, this is for illustation purpouses only
    print("You did not enter a valid age.")
    print(ex)
    print(type(ex))
else: # this part of code is executed if the except part was not executed
    print("No exceptions were encountered.")
print("Going on smoothly") # this message shows that the code is still operating and have not crashed