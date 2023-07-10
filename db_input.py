import sqlite3

dbname = 'thread.db'
conn=sqlite3.connect(dbname)
c = conn.cursor()


def db_input(num,com):
    
    sql = 'insert into threadlab (id, comment) values (?,?)'

    namelist = (num, com)
    c.execute(sql, namelist)


    conn.commit()
    
    
db_input(1,"sssss")
    