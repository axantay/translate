from telebot.types import Message
from loader import bot, db
from keyboards import get_transalte_btn



@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.save_user(user_id)
    bot.send_message(chat_id, 'Salem!', reply_markup=get_transalte_btn())
