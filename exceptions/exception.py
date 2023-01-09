# example when user enters not correct input
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError): # the ex part is considered as very technical, and may not be included, this is for illustation purpouses only
    # if in paranthese we put another type of error like ZeroDivisionError in this case, in the case of age given 0 
    # the program will authomatically give similar error message and will not crash
    print("You did not enter a valid age.")
else: # this part of code is executed if the except part was not executed
    print("No exceptions were encountered.")
