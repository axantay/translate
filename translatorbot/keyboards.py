from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def get_transalte_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Translater'))
    return markup

def register_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Register'))
    return markup

def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Contact', request_contact=True))
    return markup




def translator_btns():
    markup = InlineKeyboardMarkup()
    rus_uzb = InlineKeyboardButton('🇷🇺➡️ 🇺🇿', callback_data='ru_uz')
    rus_eng = InlineKeyboardButton('🇷🇺➡️ 🇬🇧', callback_data='ru_en')
    uzb_rus = InlineKeyboardButton('🇺🇿➡️ 🇷🇺', callback_data='uz_ru')
    uzb_eng = InlineKeyboardButton('🇺🇿➡️ 🇬🇧', callback_data='uz_en')
    eng_rus = InlineKeyboardButton('🇬🇧➡️ 🇷🇺', callback_data='en_ru')
    eng_uzb = InlineKeyboardButton('🇬🇧➡️ 🇺🇿', callback_data='en_uz')

    markup.row(rus_uzb, rus_eng)
    markup.row(uzb_rus, uzb_eng)
    markup.row(eng_rus, eng_uzb)
    return markup