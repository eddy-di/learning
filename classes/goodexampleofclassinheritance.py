from abc import ABC, abstractmethod

# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

class InvalidOperationError(Exception): # here is an example of creating your own exception error
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True
    
    def closed(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass
# The overall idea of abstract method is that it gives specific guides or rules on creating similar named methods in other classes 
# but is not iterated\run. And acts as a checks and balance instance if there will be typo eroors in other classes that has to act and iterate\run 

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
