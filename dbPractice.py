import sqlite3

connecton = sqlite3.connect('sampleDB.db')
cursor = connecton.cursor()
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
cursor.execute("""SELECT * FROM sampleTable;""")

print(cursor.fetchall())

