import sqlite3 as sql


conn = sql.connect("database.db")


cursor = conn.cursor()

clients = cursor.execute("SELECT * FROM clients;").fetchall()

print(clients)


mds = { ('1','2'): 'some1', ('2', '1'): 'some2' }

print(mds[('1','2')])