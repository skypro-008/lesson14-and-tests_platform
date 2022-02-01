import sqlite3
import os
from pathlib import Path

path = Path(os.getcwd())
path = path.joinpath('netflix.db')
con = sqlite3.connect(path)
cur = con.cursor()
sqlite_query = ("select SUM(duration) "
                "FROM netflix "
                "WHERE release_year=2010 "
                "AND `type`='Movie'")
cur.execute(sqlite_query)
minutes = cur.fetchall()[0][0]
hours = minutes // 60
result = (f'Чтобы посмотреть все фильмы, нам нужно {hours} часов.')
con.close()

if __name__ == '__main__':
    print(result)
