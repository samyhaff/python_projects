import sqlite3 as sql
conn = sql.connect('MONDIAL')
cur = conn.cursor()
req = """
SELECT c.name
FROM country c
JOIN economy e
ON e.country = 
"""
cur.execute(req)
for e in cur:
    print(e)
cur.close()
conn.close()
