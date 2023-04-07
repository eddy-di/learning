from pathlib import Path #this line allows to create and work with path objects
Path("C:\\Program Files\\Microsoft\\...") # an example of creating absolute path, writing two backslashes is a bit tedious so it is possible to use next version
Path(r"C:\Program Files\Microsoft\OneDrive") # this is an example of raw string
Path("/usr/local/bin") # absolute path for linux and mac
Path() # object that represents current folder
Path("inlib/__init__.py") # possible to access path within one main folder
Path() / Path("inlib") # combining path objects with another path
Path() / "inlib" / "combining it with another string" # combining path objects with string(s)
Path.home() #getting home directory of the user

# line 6 will be further used as main example
path = Path("inlib/__init__.py") # if there is necessity for comprehensive list just search in google for "python 3 pathlib"
path.exists() # looking if file exists or not
path.is_file() # to check if it is a file use this code
path.is_dir() # also checking directory
print(path.name) # returns only the file name -> __init__.py
print(path.stem) # returns -> __init__ without extension
print(path.suffix) # returns only extension -> .py
print(path.parent) # returns parent of path object -> inlib
# path = path.with_name("file.txt") # creates new path and overrides the previous value of path object -> inlib\file.txt (this file doesn't exist, this is only its path)
print(path) 
print(path.absolute) # getting an ebsolute value of this path
path = path.with_suffix(".txt")
print(path) # changes the extension for path from __init__.py to __init__.txt