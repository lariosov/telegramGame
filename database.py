# Импорты
import sqlite3

# Настройки БД
con = sqlite3.connect('db.sqlite', check_same_thread = False)
cur = con.cursor()

# Создаем БД
def start_database():
    # Таблица пользователей
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        USER_NAME TEXT NOT NULL,
        USER_ID TEXT NOT NULL,
        USER_BALANCE INTEGER NOT NULL,
        UNIQUE (USER_ID)
        )
    ''')
    con.commit()

    # Таблица активностей
    cur.execute('''
        CREATE TABLE IF NOT EXISTS activity(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        ACTIVITY_PRICE INTEGER NOT NULL
        )
    ''')
    con.commit()

    # Таблица магазина
    cur.execute('''
        CREATE TABLE IF NOT EXISTS shop(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        SHOP_UNIT_COST INTEGER NOT NULL
        )
    ''')
    con.commit()

    # Таблица транзакций
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TRANS_UNIT TEXT NOT NULL,
        TRANS_DATE TEXT NOT NULL,
        IS_ACTIVITY INTEGER NOT NULL,
        IS_SHOP INTEGER NOT NULL
        )
    ''')
    con.commit()
