from pathlib import Path
from time import ctime
import shutil

source = Path("Libraries/inlib/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text()) # this is an option to copy files using path and a bit noisy and tedious

shutil.copy(source, target) # another and more better way to copy with the use of shutil


# path.exists() # check if file exists, boolean value
# path.rename("__init__.txt") # renames the file
# path.unlink() # can delete it with this unlink
# print(path.stat()) #returns information about this file as stat_result object
# print(ctime(path.stat().st_ctime)) # from this stat_result object with the ctime class possible to get the human readable time of creation of the file

# path.read_bytes() # returns contents as bytes object represented in binary data
# path.read_text() # returns content of a file as a string
# path.write_bytes() 
# path.write_text(">>>>") # possible to write str
