import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

# executeメソッドでSQL文を実行する
create_table = '''create table threadlab (id value,comment verchar)'''
c.execute(create_table)

sql = 'insert into threadlab (id, comment) values (?,?)'
namelist = (1, "uma")
c.execute(sql, namelist)

conn.commit()

select_sql = 'select * from threadlab'

c.execute(select_sql)
result=c.fetchone()

conn.close()

print(result)