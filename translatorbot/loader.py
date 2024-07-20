from config import TOKEN
from telebot import TeleBot
from database import DataBase
from telebot.storage import StateMemoryStorage
from telebot import custom_filters

bot = TeleBot(TOKEN, state_storage=StateMemoryStorage())
db = DataBase()


bot.add_custom_filter(custom_filters.StateFilter(bot))
