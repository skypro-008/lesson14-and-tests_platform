import sqlite3
import prettytable
import os
from pathlib import Path

path = Path(os.getcwd())
path = path.joinpath('netflix.db')
con = sqlite3.connect(path)
cur = con.cursor()
sqlite_query = ("SELECT `title`, `release_year` FROM netflix "
                "WHERE release_year BETWEEN 1943 AND 1945 "
                "AND type='Movie'")  # TODO измените код запроса
result = cur.execute(sqlite_query)
mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
