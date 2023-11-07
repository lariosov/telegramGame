# Основные импорты
import const_text
import database
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
con = sqlite3.connect('db.sqlite', check_same_thread = False)
cur = con.cursor()


# Константы внутри бота
BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


def main():
    database.start_database()
    executor.start_polling(dp, skip_updates=True)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = const_text.INTRO_TEXT
    await message.answer(f'Привет, {message.from_user.full_name}! {text}'), first_start(message=message)


# Заполнение данных
async def first_start(message: types.Message):
    try:    
        cur.execute(f'''
            INSERT INTO users (NAME, USER_NAME, USER_ID, USER_BALANCE)
            VALUES("{message.from_user.first_name}", "{message.from_user.username}", "{message.from_user.id}", 0)
        ''')
        con.commit()
    
    except sqlite3.IntegrityError as err:
        await message.answer('Ты уже в нашей банде! Чтобы проверить баланс пиши /balance')


@dp.message_handler(commands='balance')
async def balance(message: types.Message):
    print('')
    [name], = cur.execute('''
    SELECT NAME
    FROM users
    WHERE USER_ID=?
    ''', (message.from_user.id,))
    con.commit()
    [balance], = cur.execute('''
        SELECT USER_BALANCE
        FROM users
        WHERE USER_ID=?
    ''', (message.from_user.id,))
    con.commit()
    coin = const_text.COIN_EMOJI
    await message.answer(f'Привет, {name}! У тебя: {balance} {coin}')


# Чел... это бестпрактис (нет)
if __name__ == "__main__":
    main()
