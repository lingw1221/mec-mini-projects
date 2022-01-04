# quotes.py

import sqlite3

connection = sqlite3.connect('quotes.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
              (Title TEXT, Director TEXT, Year INT)''')

connection.commit()
connection.close()
