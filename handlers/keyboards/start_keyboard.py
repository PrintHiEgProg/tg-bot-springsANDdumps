from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def get_location_kb() -> ReplyKeyboardMarkup:
    """
    get location keyboard
    """
    buttons = list()
    buttons.append([KeyboardButton(text='Отправить свои координаты 📍', request_location=True)])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def COMBO_get_many_AND_give_wedSite() -> ReplyKeyboardMarkup:
    """
    get location keyboard
    """
    buttons = list()
    buttons.append([KeyboardButton(text='Добавить новый родник 🚰')])
    buttons.append([KeyboardButton(text='Добавить новую свалку мусора 🗑️')])
    buttons.append([KeyboardButton(text='Перейти на сайт 🖼️', web_app=WebAppInfo(url='https://deanon-team.github.io'))])
    buttons.append([KeyboardButton(text='Поддержать проект 🤑', web_app=WebAppInfo(url='https://deanon-team.github.io/donat.html'))])



    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def status_water() -> ReplyKeyboardMarkup:
    """
    get location keyboard
    """
    buttons = list()
    buttons.append([KeyboardButton(text='Усох ⚫️')])
    buttons.append([KeyboardButton(text='Очень плохое 🟣')])
    buttons.append([KeyboardButton(text='Плохое 🔴')])
    buttons.append([KeyboardButton(text='Удовлетворительное 🟡')])
    buttons.append([KeyboardButton(text='Хорошое 🟢')])
    buttons.append([KeyboardButton(text='Очень хорошое ✅')])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def status_dump() -> ReplyKeyboardMarkup:
    """
    get location keyboard
    """
    buttons = list()
    buttons.append([KeyboardButton(text='Бытовые 🥤')])
    buttons.append([KeyboardButton(text='Пищевые 🍔')])
    buttons.append([KeyboardButton(text='Строительные 🏗️')])
    buttons.append([KeyboardButton(text='Токсичные ☢️')])


    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)



def resize_dump() -> ReplyKeyboardMarkup:
    """
    get location keyboard
    """
    buttons = list()
    buttons.append([KeyboardButton(text='Очень большая (> 16га) 🟣')])
    buttons.append([KeyboardButton(text='Большая (12-16га) 🔴')])
    buttons.append([KeyboardButton(text='Средняя (8-12га) 🟡')])
    buttons.append([KeyboardButton(text='Небольшая (4-8га) 🟢')])
    buttons.append([KeyboardButton(text='Мелкая (< 4га) ✅')])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def no_photo() -> ReplyKeyboardMarkup:
    """"""

    buttons = list()
    buttons.append([KeyboardButton(text='Нет фотографии')])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)









