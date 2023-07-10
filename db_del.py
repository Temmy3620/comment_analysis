import sqlite3

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()


def db_del():
    # データを削除するクエリを実行
    c.execute("delete from threadlab")

    # 変更を確定
    conn.commit()

    # 接続を閉じる
    conn.close()
    
    
    return 0

db_del()