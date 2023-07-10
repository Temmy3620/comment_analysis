import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()







        
def db_view():
    select_sql = 'select * from threadlab'

    c.execute(select_sql)
    results=c.fetchall()

    conn.close()
    
    if not results :#データが空の時
        print("None...")
    else :#データに入力があるとき
        for result in results:
            print(result)
    
db_view()