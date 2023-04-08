import sqlite3
import json
from pathlib import Path

movies = json.loads(Path(r"Libraries\inlib\movies.json").read_text())

with sqlite3.connect(r"Libraries\inlib\db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
# lines from 7-11 show the code to input json format into sqslite3 db

with sqlite3.connect(r"Libraries\inlib\db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row) # result will be in tuples
    movies = cursor.fetchall()
    print(movies) # this result gives list of tuples