class Phone:
# this is an example of a class attributes (аттрибуты класса, присущи всем созданным объектам) first 8 videos of Mosh Hamedani on classes  
    material = "metal"

    # line with def __init__(self, model, price, os): is and example of instance attributes function (пример отдельного случая\экземпляра класса)
    def __init__(self, model, price, os): # the double undescored methods like __init__ or __str__ are called magic methods
        self.model = model
        self.price = price
        self.os = os
        pass
# Further part shows a class method/class function with decorator that starts with @ with it we can put the initial value to all created objects
    @classmethod
    def initial_value(cls):
        return cls("Not Available", 0, "Not Available")
# with this method we can transform the given values to objects as a string type output    
    def __str__(self): # __str__ magic method converts the object inside values into string
        return f"{self.model}, {self.price}, {self.os}"
    
    def __gt__(self, other): # also if you put the opposite less than sign the opposite of this logic works smoothly
        return self.price > other.price

    def __eq__(self, other): # the mgic methods like __gt__ or __eq__ allow to compare parameters that you want to be compared in this case I wanted to make comparison of only prices
        return self.price == other.price
# __add__ function works just like normal logical operator both with intigers and strings. Specific parameters can be also added, but with specifically inquiring to them like phone1.model + phone2.model    
    def __add__(self, other):
        return self.price + other.price

    def info(self):
        print(f"Info on {self.model}, it's price is {self.price}, and it runs on {self.os}")

phone1 = Phone("Redmi", 10000, "Android OS")
phone1.info()
phone2 = Phone("iPhone", 100000, "iOS")
print(phone1, phone2, sep="\n")
print(phone1.model + phone2.model)