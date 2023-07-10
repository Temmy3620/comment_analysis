import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

# executeメソッドでSQL文を実行する
create_table = '''create table threadlab (date verchar,time verchar,comment verchar)'''
c.execute(create_table)

sql = 'insert into threadlab (date, time, comment) values (?,?,?)'
namelist = ("2023/06/10(土)","00:34:50", "uma")
c.execute(sql, namelist)

conn.commit()

select_sql = 'select * from threadlab'

c.execute(select_sql)
result=c.fetchone()

conn.close()

print(result)