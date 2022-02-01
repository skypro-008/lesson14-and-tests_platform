import sqlite3
import os
from pathlib import Path

path = Path(os.getcwd())
path = path.joinpath('netflix.db')
con = sqlite3.connect(path)
cur = con.cursor()
sqlite_query = ("select SUM(duration) "
                "FROM netflix "
                "WHERE director='Alastair Fothergill' "
                "AND `type`='TV Show'")
cur.execute(sqlite_query)
seazons = cur.fetchall()[0][0]
result = ('Длительность всех сериалов режиссера Alastair Fothergill'
          f' составляет {seazons} сезона.')
con.close()

if __name__ == '__main__':
    print(result)
