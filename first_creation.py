import sqlite3

DBNAME = "domovoy_bot.db"


def first_creation():
    try:
        with sqlite3.connect(DBNAME) as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE users("
                           "user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                           "tg_id INT NOT NULL, "
                           "name TEXT NOT NULL)")
            cursor.execute("CREATE TABLE notes("
                           "note_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                           "user_id INT NOT NULL, "
                           "title TEXT NOT NULL, "
                           "description TEXT NOT NULL,"
                           "date DATETIME NOT NULL)")
            cursor.execute("CREATE TABLE photos("
                           "photo_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                           "photo BLOB NOT NULL, "
                           "note_id INT NOT NULL)")
            conn.commit()
            return {"status": "ok"}
    except Exception as ex:
        return {"status": ex.args[0]}
    finally:
        conn.close()