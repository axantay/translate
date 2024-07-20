import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='awdarma_bot',
            user='postgres',
            host='localhost',
            password='123456789'
        )

    def manager(self, sql, *args, commit: bool = False,
                fetchone: bool = False,
                fetchall: bool = False):

        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    return db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()


    def create_table_users(self):

        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            full_name VARCHAR(60),
            contact VARCHAR(15) UNIQUE
        )'''

        self.manager(sql, commit=True)


    def save_user(self, telegram_id):
        sql = '''INSERT INTO users(telegram_id)
        VALUES (%s)
        ON CONFLICT DO NOTHING'''

        self.manager(sql, (telegram_id,), commit=True)


    def check_user(self, telegram_id):

        sql = '''SELECT * FROM users WHERE telegram_id = %s'''
        return self.manager(sql, telegram_id, fetchone=True)


    def register_user(self, full_name, contact, telegram_id):

        sql = '''UPDATE users SET full_name=%s, contact=%s, telegram_id=%s'''
        self.manager(sql, full_name, contact, telegram_id, commit=True)
