import json
from pathlib import Path
import shutil

# source = Path("files.zip")
# target = Path(r"Libraries\inlib\files.zip")

# shutil.move(source, target)

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990},
# ] # created json dictionaries in array

# data = json.dumps(movies) # made an object with the json format of previous information

# Path(r"Libraries\inlib\movies.json").write_text(data) # with the given directory saved the json file

data = Path(r"C:\Users\Eddy.di\Downloads\sample1.json").read_text()
mov = Path(r"Libraries\inlib\movies.json").read_text()
sample1 = json.loads(data)
movies = json.loads(mov)
print(sample1)
print(movies[0]["title"])