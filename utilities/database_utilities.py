#!/usr/bin/python3
import sqlite3


def create_words_table(db):
    del_table = 'DROP TABLE IF EXISTS words'
    sql = "CREATE TABLE 'words' ('word' TEXT NOT NULL UNIQUE,\
                                'usage_count' INTEGER NOT NULL DEFAULT 1,\
                                PRIMARY KEY('word'));"
    index = "CREATE UNIQUE INDEX 'words_word_index' ON 'words' ('word');"

    db.execute(del_table)
    print('"{}" table has been removed'.format('words'))

    db.execute(sql)
    db.execute(index)
    print('A new table created: "{}"'.format('words'))
    db.commit()


def create_database(database_path: str):
    """
    Generates the database
    :type database_path: object str
    """
    db = None
    try:
        db = sqlite3.connect(database_path)
        print('DB connection opened')
        create_words_table(db)
        print('SQLite version: {}'.format(sqlite3.version))
    except Exception as e:
        print(e)
    finally:
        if db is not None:
            db.close()
            print('DB connection closed')


def save_words_to_database(database_path: str, words_list: list):
    """
    Save the word to DB
    :type database_path: object str
    :type words_list: object list
    """

    db = sqlite3.connect(database_path)
    with db:
        cursor = db.cursor()
        for word in words_list:
            # check is word in DB already
            sql = "SELECT COUNT(*) FROM {} WHERE word='{}'".format('words', word)
            cursor.execute(sql)
            count = cursor.fetchone()[0]

            if count > 0:
                sql = "UPDATE {} SET {} = {} + 1 WHERE {} = '{}'"\
                    .format('words', 'usage_count', 'usage_count', 'word', word)
            else:
                sql = "INSERT INTO {}({}) VALUES('{}')".format('words', 'word', word)

            # print(sql)
            cursor.execute(sql)

    print('Database save complete')

    if db is not None:
        db.close()
