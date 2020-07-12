import sqlite3


# Запрос на уникальные города в списке базы
def checkCity():
    db = sqlite3.connect('PlacesDatabase.db')
    sql = db.cursor()
    msg = '<b>Я помню о местах в следующих городах:</b>\n'
    for value in sql.execute('SELECT city FROM CoolPlaces GROUP BY city HAVING COUNT(*)=1'):
        msg = msg + value[0] + '\n'
    return msg


# Запрос на город + место + описание
def showCityPlaces():
    db = sqlite3.connect('PlacesDatabase.db')
    sql = db.cursor()

    for value in sql.execute('SELECT city,place,desc FROM CoolPlaces'):
        msg = msg + value[0] + value[1] + value[2] + '\n'
    return msg

# def initialization():
#     db = sqlite3.connect('PlacesDatabase.db')
#     sql = db.cursor()
#
#     sql.execute(""" CREATE TABLE IF NOT EXISTS CoolPlaces (
#                 ID INTEGER UNIQUE,
#                 city TEXT NOT NULL,
#                 place TEXT NOT NULL,
#                 desc TEXT NOT NULL,
#                 PRIMARY KEY("ID" AUTOINCREMENT)
#                 )
#     """)
#     db.commit()
