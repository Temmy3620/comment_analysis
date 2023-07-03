import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

sql = 'insert into threadlab (id, comment) values (?,?)'
namelist = (1, "uma")
c.execute(sql, namelist)

conn.commit()
