from modes.mod1 import calc_shipping, calc_tax
import modes.mod1
# or u can also import in a different fashion
# packages and the way how to access them when you move modules to another file, need to create __init__.py file for a better functionality
from modes import mod1
import sys
# this is an example of using modules (mod1.py) in python and using them, with the ability to utilize created functions, classes or variables
mod1.calc_shipping()
mod1.calc_tax()

modes.mod1.calc_shipping()
modes.mod1.calc_tax()

# after opening of the file in terminal the __pycache__ appers, it is necessary to access faster to the imported modules
print(sys.path) # this shows where python will be looking for other modules when they are imported to project
calc_tax()
calc_shipping()