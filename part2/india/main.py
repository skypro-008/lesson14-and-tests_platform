# Болливуд
#
# Индийские фильмы одно время были очень популярны.
# Давайте проверим, как это отразилось на Нетфликсе!
# Нам нужно посчитать, сколько индийских фильмов и сериалов есть на платформе.
#
# Пример результата:
#
# фильмы: 50 шт
# сериалы: 10 шт
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3
import os
from pathlib import Path

path = Path(os.getcwd())
path = path.joinpath('netflix.db')
con = sqlite3.connect(path)
cur = con.cursor()
sqlite_query = ("")  # TODO измените код
cur.execute(sqlite_query)
executed_query = cur.fetchall()

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

result = ""

con.close()

if __name__ == '__main__':
    print(result)
