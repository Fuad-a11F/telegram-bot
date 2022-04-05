import logging

from aiogram import Bot, Dispatcher, executor, types
from checkMessage import ValidationMessage
from constant import API_TOKEN

validation = ValidationMessage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f"Добавлен новый пользователь с никнеймом {message.from_user.username}")


@dp.message_handler()
async def echo(message: types.Message):
    text_received = message.text
    print(message.text)
    if validation.check_message(text_received, message.from_user.id):
        await message.answer(validation.get_text(message.from_user.username))
        await message.delete()

    elif validation.user_blocked(message.from_user.id):
        await message.answer(validation.get_blocked_text(message.from_user.username, message.from_user.id))
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
