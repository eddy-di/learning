#There are global and local variables and the practice 
#of naming variables in a right manner comes into play 
#in such situations, so that Python will be able 
#to run code smoothly.
message = "Hello World"

def greet (name):
    message = f"Hello {name}"


print (message)
#in this example there is bad naming of global variable message
# in line5 and the local variable in line8 message is also 
#named like this. Avoid such practise.