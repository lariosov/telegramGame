# Основные импорты
import const_text
import sqlite3
import aiogram
import os

# Основные под-импорты
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv


# Подгружаем енв переменные
load_dotenv()


# Настройки БД
con = sqlite3.connect('db.sqlite', check_same_threads = False)
cur = con.cursor()


# Создаем БД
def start_database():
    # Создаем таблицу пользователей
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        USER_NAME TEXT NOT NULL,
        USER_ID TEXT NOT NULL,
        USER_BALANCE INTEGER NOT NULL
        );
    ''')
    con.commit()

    # Создаем таблицу активностей
    cur.execute('''
        CREATE TABLE IF NOT EXISTS activity(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        ACTIVITY_PRICE INTEGER NOT NULL
        );
    ''')
    con.commit()

    # Создаем таблицу магазина
    cur.execute('''
        CREATE TABLE IF NOT EXISTS shop(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT,
        SHOP_UNIT_COST INTEGER NOT NULL
        );
    ''')
    con.commit()


# Константы внутри бота
BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


def main():
    executor.start_polling(dp, skip_updates=True)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = const_text.INTRO_TEXT
    await message.answer(f'Привет, {message.from_user.full_name}! {text}')


# Чел... это бестпрактис (нет)
if __name__ == "__main__":
    main()
