import sqlite3
from datetime import datetime

DBNAME = 'domovoy_bot.db'


class User:
    # initialization
    def get_by_tg_id(self, tg_id):
        """
       Инициализация объекта класса и проверка есть ли пользователь с данным tg_id в базе данных
       На выход:
       {"status": "ok"}
       {"status": "user not found"}
       {"status": unknown error}
       """
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                assert type(tg_id) == int, "invalid type for tg_id"
                cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
                if cursor.fetchone():
                    conn.commit()
                    self.tg_id = tg_id
                    return {"status": "ok"}
                return {"status": "user not found"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def add_user(self, tg_id: int, name: str):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                assert type(tg_id) == int, "invalid type for tg_id"
                assert type(name) == str, "invalid type for name"
                cursor.execute("INSERT INTO users(tg_id, name) VALUES (?, ?)", (tg_id, name))
                conn.commit()
                return {"status": "ok"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def get_name(self):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM users WHERE tg_id = ?", (self.tg_id,))
                out = cursor.fetchone()[0]
                if out:
                    conn.commit()
                    return {"status": "ok", "out": out}
                return {"status": "result in None"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def get_user_by_user_id(self, user_id: int):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                assert type(user_id) == int, "invalid type for user_id"
                cursor.execute("SELECT tg_id FROM users WHERE user_id = ?", (user_id,))
                out = cursor.fetchone()[0]
                if out:
                    user = User()
                    user.get_by_tg_id(out)
                    conn.commit()
                    return {"status": "ok", "out": user}
                return {"status": "user not found"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

class Note:

    def get_by_title(self, title: str):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                assert type(title) == str, "invalid type for title"
                cursor.execute("SELECT note_id FROM notes WHERE title = ?", (title,))
                if cursor.fetchone():
                    self.title = title
                    conn.commit()
                    return {"status": "ok"}
                return {"status": "user not found"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def add_note(self, user_id: int, title: str, description: str, date: datetime):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                assert type(user_id) == int, "invalid type for user_id"
                assert type(title) == str, "invalid type for title"
                assert type(description) == str, "invalid type for description"
                assert type(date) == datetime, "invalid type for date"
                cursor.execute("SELECT note_id FROM notes WHERE title = ?", (title, ))
                if cursor.fetchone():
                    return {"status": "title exists"}
                cursor.execute("INSERT INTO notes(user_id, title, description, date) VALUES (?, ?, ?, ?)", (user_id, title, description, date))
                conn.commit()
                return {"status": "ok"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def get_description(self):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT description FROM notes WHERE title = ?", (self.title, ))
                out = cursor.fetchone()[0]
                if out:
                    conn.commit()
                    return {"status": "ok", "out": out}
                return {"status": "result in None"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

    def get_date(self):
        try:
            with sqlite3.connect(DBNAME) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT date FROM notes WHERE title = ?", (self.title, ))
                out = cursor.fetchone()[0]
                if out:
                    conn.commit()
                    return {"status": "ok", "out": out}
                return {"status": "result in None"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()
