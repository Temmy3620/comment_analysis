import sqlite3

#関数化したい

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

sql = 'insert into threadlab (id, comment) values (?,?)'

namelist = (1, "uma")
c.execute(sql, namelist)

namelist2 = (2, "uma2")
c.execute(sql, namelist2)

conn.commit()
