from telebot.handler_backends import StatesGroup, State


class RegisterStates(StatesGroup):
    name = State()
    lastname = State()
    contact = State()