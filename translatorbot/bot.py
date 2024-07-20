from loader import db, bot

db.create_table_users()

import handlers

if __name__ == '__main__':
    bot.infinity_polling()