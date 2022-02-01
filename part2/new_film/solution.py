import sqlite3
import os
from pathlib import Path

path = Path(os.getcwd())
path = path.joinpath('netflix.db')
con = sqlite3.connect(path)
cur = con.cursor()
sqlite_query = ("SELECT `title` from netflix "
                "order by `date_added` DESC LIMIT 1")
result = cur.execute(sqlite_query)
result = cur.fetchall()
movie_title = result[0][0]
result = (f'{movie_title}')
con.close()

if __name__ == '__main__':
    print(result)
