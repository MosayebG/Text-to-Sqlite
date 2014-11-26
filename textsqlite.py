#!/usr/bin/env python
# -*- coding: utf_8 -*-

import sqlite3 as lite
import sys

if (len(sys.argv)) != 3:
    print "Usage: ./textsqlite.py <textfile> <database>"
    exit(0)


def to_db(my_file, database):

    conn = lite.connect(database)
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute("CREATE TABLE table1(Id INTEGER PRIMARY KEY NOT NULL , cat INTEGER, fav INTEGER, tex CHAR);")

    my_file = open(my_file, 'r')
    my_file_text = my_file.read()

    file_len = len(my_file_text)

    for i in range(0, file_len):
        if i == file_len - 1:
            t = my_file_text[first:i+1]
            cur.execute("INSERT INTO table1 (cat, fav, tex) VALUES (0, 0, ?);", (t, ))

        if my_file_text[i] == '\n':
            t = my_file_text[first:i]
            first = i
            cur.execute("INSERT INTO table1 (cat, fav, tex) VALUES (0, 0, ?);", (t, ))

    conn.commit()

to_db(sys.argv[1], sys.argv[2])
