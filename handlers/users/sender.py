import asyncio
from aiogram import types
from aiogram.types import ContentType, Message
import sqlite3
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext


channel_ids = []

ides = db.select_all_users()
for ids in ides:
    channel_ids.append(ids[0])


from data.config import ADMINS

time = 1

time = time * 600

@dp.message_handler(text='set_time')
async def stop(message: types.Message):
    times = 0
    user_id = message.chat.id
    if str(user_id)in ADMINS:
        try:
            times = int(message.text)
            time = times * 3600
            await bot.send_message(chat_id=user_id, text=f"Xabar jonatish vaqti o'rnatildi..({times} soat)")
        except:
            await bot.send_message(chat_id=user_id, text="Xabar jonatish soat vaqtini kiriting(faqat son kiriting) ")
    else:
        await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")

        
@dp.message_handler(text='stop_sended')
async def stop(message: types.Message):
    user_id = message.chat.id
    if str(user_id)in ADMINS:
        db.update_activ('0')
        await bot.send_message(chat_id=user_id, text="Xabar jonatish to'xtadi...")
    else:
        await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")

@dp.message_handler(text='start_sender')
async def stop(message: types.Message):
    user_id = message.chat.id
    if str(user_id)in ADMINS:
        db.update_activ('1')
        await bot.send_message(chat_id=user_id, text="Avtomatik habar jo'natish yondi...")
    else:
        await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")


@dp.message_handler(text='reklama')
async def send_reklama():
    @dp.message_handler(content_types='photo')
    async def photo_handler(message: types.Message):
        user_id = message.chat.id
        text = message.caption
        photos = message.photo[-1].file_id
        ishora = db.select_all_activ()[0][0]
        if str(user_id) in ADMINS:
            if message.caption:
                while ishora:
                    timer = time
                    channel_ids = []
                    ides = db.select_all_users()
                    for ids in ides:
                        channel_ids.append(ids[0])
                    for channel_id in channel_ids:
                        try:
                            await bot.send_photo(chat_id=channel_id, caption=text,
                                                photo=photos)
                        except:
                            await bot.send_message(chat_id=user_id, text="Kechirasiz bu kanalda bot yoq \nshu sababli habar jonata olmayman..")
                    await asyncio.sleep(timer)
            else:
                while ishora:
                    timer = time
                    channel_ids = []
                    ides = db.select_all_users()
                    for ids in ides:
                        channel_ids.append(ids[0])
                    for channel_id in channel_ids:
                        try:
                            await bot.send_photo(chat_id=channel_id,
                                                photo=photos)
                        except:
                            await bot.send_message(chat_id=user_id, text="Kechirasiz bu kanalda bot yoq \nshu sababli habar jonata olmayman..")
                    await asyncio.sleep(timer)
        else:
            await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")


    @dp.message_handler(content_types='text')
    async def main_func(message: types.Message):
        user_id = message.chat.id
        ishora = db.select_all_activ()[0][0]
        if str(user_id) in ADMINS:
            text = message.text
            while ishora == 1:
                timer = time
                channel_ids = []
                ides = db.select_all_users()
                for ids in ides:
                    channel_ids.append(ids[0])
                try:                    
                    for channel_id in channel_ids:
                        await bot.send_message(chat_id=channel_id, text=text)
                except:
                    await bot.send_message(chat_id=user_id, text=f"Kechirasiz bu kanalda bot yoq \nshu sababli habar jonata olmayman..")
                await asyncio.sleep(timer)
                ishora = db.select_all_activ()[0][0]
        else:
            await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")


    @dp.message_handler(content_types='video')
    async def video_send(message: types.Message):
        user_id = message.chat.id
        ishora = db.select_all_activ()[0][0]
        if str(user_id) in ADMINS:
            if message.caption:
                text = message.caption
                video = message.video.file_id
                while True:
                    timer = time
                    channel_ids = []
                    ides = db.select_all_users()
                    for ids in ides:
                        channel_ids.append(ids[0])
                    for channel_id in channel_ids:
                        try:
                            await bot.send_video(chat_id=channel_id, video=video, caption=text)
                        except:
                            await bot.send_message(chat_id=user_id, text="Kechirasiz bu kanalda bot yoq \nshu sababli habar jonata olmayman..")
                    await asyncio.sleep(timer)
            else:
                video = message.video.file_id
                while True:
                    channel_ids = []
                    ides = db.select_all_users()
                    for ids in ides:
                        channel_ids.append(ids[0])
                    for channel_id in channel_ids:
                        try:
                            await bot.send_video(chat_id=channel_id, video=video)
                        except:
                            await bot.send_message(chat_id=user_id, text="Kechirasiz bu kanalda bot yoq \nshu sababli habar jonata olmayman..")
                    await asyncio.sleep(timer)
        else:
            await bot.send_message(chat_id=user_id, text="Kechirasiz siz Admin emassiz...")
