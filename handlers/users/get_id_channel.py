import sqlite3
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_button import menuPython

channel_ids = []


@dp.message_handler(text='menu')
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menuPython)


@dp.message_handler(text='add_channel')
async def set_state(msg: types.Message, state: FSMContext):
    """Foydalanuvchini biro state ichiga kirgizamiz"""
    await state.set_state('add_channels')
    await msg.answer('Menga kanaldan habar forward qiling men uni bazaga qoshib qoyaman.. ')
    

@dp.message_handler(state='add_channels')
async def get_channel_id(message: types.Message, state: FSMContext):
    ides = db.select_all_users()
    for ids in ides:
        channel_ids.append(ids[0])
    
    try:
        if message.forward_from_chat.id not in channel_ids:
            if message.forward_from_chat.type == 'channel':
                title = message.forward_from_chat.title 
                db.add_user(channel_id=message.forward_from_chat.id, channel_name=title)
                await bot.send_message(chat_id=message.chat.id, text=f"Bu {title}  Kanal Muvafaqqiyatli qoshildi....")
            else:
                await bot.send_message(chat_id=message.chat.id, text="Bu Kanaldan kelgan habar emas....")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Bu kanal bazada mavjud boshqa tashlang..")
    except:
        await bot.send_message(chat_id=message.chat.id, text="Bu Notog'ri Xabar..")
    
    
    await state.finish()
