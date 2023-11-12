#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('ironsharp.db')
print("Opened database successfully")

# conn.execute('''
#     DROP TABLE IF EXISTS user;
#          ''')
# conn.execute('''
#     DROP TABLE IF EXISTS products;
#          ''')

# conn.execute('''
#     CREATE TABLE user (
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       username TEXT UNIQUE NOT NULL,
#       password TEXT NOT NULL);
#          ''')

# conn.execute('''
#   CREATE TABLE products (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   body TEXT NOT NULL,
#   price REAL NOT NULL, 
#   quantity INTEGER NOT NULL
# );
#          ''')
print(f"{conn.execute('''select * from user;''')}")

      


conn.close()



