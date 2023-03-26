class Product:
    def __init__(self, price):
        self.price = price
# There are times when users may input negative values to product prices. Python accepts it but we need to create a logic of making it not possible
# third option is to create properties in a class and make it work just like the line with price = property(get_price, set_price)
    @property
    def price(self): # This method takes an input from a user
        return self.__price
    @price.setter
    def price(self, value):
        if value < 0: # This part checks if the price is negative, and if it is like that, will give an error to a user
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(100)
product.price = -1
print(product.price)