from pathlib import Path

path = Path("Libraries/inlib")
# path.exists() # returns a boolean
# path.mkdir() # make directory
# path.rmdir() # remove directory
# path.rename("inlibrary")
print(path.iterdir()) # can get the list of files and methods in this path and if you print it you will get generator object
for p in path.iterdir(): # iterate over the names in file and giving their paths
    print(p)

paths = [p for p in path.iterdir()] # this is a list comprehension example that allows to create array of WindowsPath
# 2 limitations 1. cannot search by a pattern, 2. it does not search recursively
# print(paths)
# for the scenarios mentioned in line 13 need to use glob method
path.glob("*.*") # search for all files
path.glob("*.py") # search for all py files
py_files = [p for p in path.glob("**/*.py")] # "**/*.py" this allows to search recursively
print(py_files)
py_files = [p for p in path.rglob("*.py")] # this is another way of making the same type of line like in 18
print(py_files)