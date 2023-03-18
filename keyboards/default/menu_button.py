from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            
            KeyboardButton(text="add_channel"),
            KeyboardButton(text="send_reklama"),
        ],
        [
            KeyboardButton(text="set_time"),
            KeyboardButton(text="start_sender"),
            KeyboardButton(text="stop_sended"),
        ]
    ],
    resize_keyboard=True
)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="menu"),
        ],
    ],
    resize_keyboard=True
)
