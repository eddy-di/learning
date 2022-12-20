def increment (number, by=1):
    #in this case, the by+1 parameter is optional and 
    #on line 6 you can not define or write it will automatically put 1
    return number + by


print(increment(2, by=1)) #by=1 is a keyword argument when lots of arguments 
#are used, to read and understand code better and faster