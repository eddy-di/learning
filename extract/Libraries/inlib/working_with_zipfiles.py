from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w") # this statement creates a zip file in a folder

# for path in Path("inlib").rglob("*.*"):
#     zip.write(path)
# zip.close()
# lines 6-8 are the example of making a zip file of inlib file that is in Libraries folder
# there is another way of doing it without calling zip.close() statement
 
with ZipFile("files.zip", "w") as zip: # "w" means open and write
    for path in Path("Libraries/inlib").rglob("*.*"):
        zip.write(path)
# this way allows to create a zip file of the folder that is stated in for statment without need of closing it

with ZipFile("files.zip") as zip:
    print(zip.namelist())
