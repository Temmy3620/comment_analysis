import sqlite3

dbname = 'thread.db'
conn=sqlite3.connect(dbname)
c = conn.cursor()


def db_input(date,time,com):
    
    sql = 'insert into threadlab (date, time, comment) values (?,?,?)'

    namelist = (date, time, com)
    c.execute(sql, namelist)


    conn.commit()
    
    
db_input("2023/06/10(土)","00:34:50","sss\\\ss")
    