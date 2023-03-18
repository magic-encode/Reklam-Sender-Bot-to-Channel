import sqlite3
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_button import menu



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Xush kelibsiz {name}!", reply_markup=menu)


    