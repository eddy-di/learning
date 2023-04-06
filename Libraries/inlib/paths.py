from pathlib import Path #this line allows to create and work with path objects
# an example of creating absolute path
Path("C:\\Program Files\\Microsoft\\...") #writing two backslashes is a bit tedious so it is possible to use next version
Path(r"C:\Program Files\Microsoft\OneDrive") # this is an example of raw string
Path("/usr/local/bin") # absolute path for linux and mac
Path() # object that represents current folder
Path("inlib/__init__.py") # possible to access path within one main folder
Path() / Path("inlib") # combining path objects with another path
Path() / "inlib" / "combining it with another string" # combining path objects with string(s)
Path.home() #getting home directory of the user

