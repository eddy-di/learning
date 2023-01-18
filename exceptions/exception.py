# example when user enters not correct input
try:
    file = open("exception.py") # this is an example of file or other resource been used in a code and it opens it
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex: # the ex part is considered as very technical, and may not be included, this is for illustation purpouses only
    # if in paranthese we put another type of error like ZeroDivisionError in this case, in the case of age given 0 
    # the program will authomatically give similar error message and will not crash
    print("You did not enter a valid age.")
    print(type(ex))
else: # this part of code is executed if the except part was not executed
    print("No exceptions were encountered.")
finally: # this statement is executed even if exception was or wasn't executed and it closes the resource that was opened prior
    file.close()