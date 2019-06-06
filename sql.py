import sqlite3 as sql

conn = sql.connect('MONDIAL')
cur = conn.cursor()
req = """

"""
cur.execute(req)
for e in cur:
    print(e)
cur.close()
conn.close()
