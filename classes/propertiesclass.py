class Product:
    def __init__(self, price):
        self.set_price(price)
# There are times when users may input negative values to product prices. Python accepts it but we need to create a logic of making it not possible
    def get_price(self): # This method takes an input from a user
        return self.__price
    def set_price(self, value):
        if value < 0: # This part checks if the price is negative, and if it is like that, will give an error to a user
            raise ValueError("Price cannot be negative.")
        self.__price = value
# one of the ways of implementing a code. But this way is considered as a bit noisy and not pythonic
    price = property(get_price, set_price) # this is considered as more pythonic in a sense

product = Product(100)
print(product.price)