import sqlite3

import requests
from bs4 import BeautifulSoup

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()

sql = 'insert into threadlab (id, comment) values (?,?)'



# Webページを取得して解析する

load_url = "https://jbbs.shitaraba.net/bbs/read_archive.cgi/anime/11133/1686317062/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
#print(soup)

#coment = soup.find("dd")

#print(coment)

cnt = 1

for element in soup.find_all("dd"):    # その中のliタグの文字列を表示
    print(element.text)
    namelist = (cnt, element.text)
    c.execute(sql, namelist)
    conn.commit()

    cnt = cnt + 1
