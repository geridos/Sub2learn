#!/usr/bin/python3.5

import readchar
import re
import os.path
import sqlite3
from sqlite3 import Error

user_data_base="user/learn.db"

know_words_table="know_words"
unknow_words_table="unknow_words"

#TODO close opened file/database

sql_create_known_table = """ CREATE TABLE IF NOT EXISTS known_words (
                                        id integer PRIMARY KEY,
                                        word text NOT NULL,
                                    ); """


sql_create_unknown_table = """ CREATE TABLE IF NOT EXISTS unknown_words (
                                        id integer PRIMARY KEY,
                                        word text NOT NULL,
                                    ); """

def check_if_word_here(conn, table, word):
    request = "select " + word + " from " + table
    try:
        c = conn.cursor()
        c.execute(request)
        rows = c.fetchall()
        print(row)
    except Error as e:
        print(e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def setup_db():
    conn = create_connection(user_data_base)
    create_table(conn, sql_create_known_table)
    create_table(conn, sql_create_unknown_table)

def get_database_unknow_words():
    pass

def add_words_in_know_database(word):
    pass

def add_words_in_unknow_database(word):
    pass

def parser(file):
    text = ""
    with open(file) as f:
        text = f.read().lower()
    print(text)

    array = re.split('\.|, | |\.\n|\s|\(|\)', text)
    set_text = set(array)

    nodig_array = []
    for a in set_text:
        if a.isdigit() == False and len(a) > 1:
            nodig_array.append(a)

    print(nodig_array)




    return nodig_array

def user_action():
    words = parser("file.txt")
    print("press k=known, u=unknow, e=to exit")
    i = 0
    while True:
        if i >= len(words):
            break
        print(words[i])
        x = readchar.readchar()

        if x == "k":
            add_words_in_know_database(words[i])
        elif x == "u":
            add_words_in_unknow_database(words[i])
        elif x == "e":
            break
        else:
            print("unknow option")
        i = i+1


setup_db()
user_action()
