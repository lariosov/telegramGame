# Основные импорты
import const_text
import aiogram
import os

# Основные под-импорты
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv


load_dotenv()


# Константы внутри бота
BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


def main():
    executor.start_polling(dp, skip_updates=False)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = const_text.INTRO_TEXT
    await message.answer(f'Привет, {message.from_user.full_name}! {text}')


# Чел... это бестпрактис (нет)
if __name__ == "__main__":
    main()
