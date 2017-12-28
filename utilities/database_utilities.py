#!/usr/bin/python3
import sqlite3
import os


def create_words_table(db):
    sql = "CREATE TABLE 'words' ('word' TEXT NOT NULL UNIQUE,\
                                'usage_count' INTEGER NOT NULL DEFAULT 1,\
                                PRIMARY KEY('word'));"
    db.execute(sql)
    db.commit()


def create_database(database_path: str):
    """
    Generates the database
    :type database_path: object str
    """
    try:
        if not os.path.exists(database_path):
            db = sqlite3.connect(database_path)
            create_words_table(db)
            print('A new database is created: {}'.format(database_path))
        print('SQLite version: {}'.format(sqlite3.version))
    except Exception as e:
        print(e)
    finally:
        db.close()


def save_words_to_database(database_path: str, words_list: list):
    """
    Save the word to DB
    :type database_path: object str
    :type words_list: object list
    """
    # TODO: save the word to DB
    pass
