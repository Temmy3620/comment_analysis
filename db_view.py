import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()


select_sql = 'select * from threadlab'

c.execute(select_sql)
result=c.fetchone()

conn.close()

print(result)