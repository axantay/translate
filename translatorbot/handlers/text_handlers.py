from telebot.types import Message, ReplyKeyboardRemove, CallbackQuery
from loader import bot, db
from translate import Translator

from states import RegisterStates

from keyboards import *


@bot.message_handler(func=lambda message: message.text == 'Translater')
def reaction_translate(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    check = db.check_user(user_id)
    if None in check:
        bot.send_message(chat_id, 'Iltimas, botti isletiw ushin dizimnen otin\'', reply_markup=register_btn())
    else:
        bot.send_message(chat_id, '⏳', reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "Tillerdi saylan\'!", reply_markup=translator_btns())







@bot.message_handler(func=lambda message: message.text == 'Register')
def reaction_register(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    bot.set_state(user_id, RegisterStates.name, chat_id)
    bot.send_message(chat_id, 'Atinin\'izdi jazin\'!', reply_markup=ReplyKeyboardRemove())



@bot.message_handler(content_types=['text'], state=RegisterStates.name)
def reaction_name_(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    with bot.retrieve_data(user_id, chat_id) as data:
        data['name'] = message.text.capitalize()

    bot.set_state(user_id, RegisterStates.lastname, chat_id)
    bot.send_message(chat_id, 'Familyan\'izdi kiritin\':')

@bot.message_handler(content_types=['text'], state=RegisterStates.lastname)
def reaction_lastname(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    with bot.retrieve_data(user_id, chat_id) as data:
        data['lastname'] = message.text.capitalize()

    bot.set_state(user_id, RegisterStates.contact, chat_id)
    bot.send_message(chat_id, 'Nomerin\'izdi kiritin\':', reply_markup=send_contact())

@bot.message_handler(content_types=['text', 'contact'], state=RegisterStates.contact)
def reaction_contact(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id


    with bot.retrieve_data(user_id, chat_id) as data:
        name = data['name']
        lastname = data['lastname']
        contact = message.contact.phone_number
        full_name = f"{name} {lastname}"
        db.register_user(full_name, contact, user_id)

    bot.delete_state(user_id, chat_id)
    bot.send_message(chat_id, 'Isletsen\'iz boladi!', reply_markup=get_transalte_btn())

@bot.callback_query_handler(func=lambda call: call.data in ['ru_uz', 'ru_en',
                                                            'uz_ru', 'uz_en',
                                                            'en_ru', 'en_uz'])

def reaction_callbacks(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_lang, to_lang = call.data.split('_')
    msg = bot.send_message(chat_id, 'So\'z kiritin\':')
    bot.register_next_step_handler(msg, get_translate, from_lang, to_lang)


def get_translate(message: Message, from_lang, to_lang):
    chat_id = message.chat.id
    try:
        word = message.text
        translate = Translator(to_lang, from_lang=from_lang)
        translated_word = translate.translate(word)
        bot.send_message(chat_id, translated_word, reply_markup=get_transalte_btn())
    except:
        bot.send_message(chat_id, 'Qa\'telik!')









