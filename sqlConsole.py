import sqlite3 as sql

conn = sql.connect('MONDIAL')
cur = conn.cursor()
while True:
    req = input("requete SQL ou stop pour quitter: ")
    if req == "stop":
        break
    try:
        cur.execute(req)
    except:
        print("erreur")
    else:
        for enreg in cur:
            print(enreg)
    print()
cur.close()
conn.close()
