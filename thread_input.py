import sqlite3

import requests
from bs4 import BeautifulSoup

dbname = 'thread.db'

conn=sqlite3.connect(dbname)
c = conn.cursor()
"""
sql = 'insert into threadlab (id, comment) values (?,?)'

# Webページを取得して解析する
load_url = "https://jbbs.shitaraba.net/bbs/read_archive.cgi/anime/11133/1686317062/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


for element in soup.find_all("dd"):    # その中のliタグの文字列を表示
    print(element.text)
    
"""
def thread_input(load_url):
    
    sql = 'insert into threadlab (id, comment) values (?,?)'

    # Webページを取得して解析する
    #load_url = "https://jbbs.shitaraba.net/bbs/read_archive.cgi/anime/11133/1686317062/"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")


    for element in soup.find_all("dd"):    # その中のliタグの文字列を表示
        print(element.text)
    
thread_input("https://jbbs.shitaraba.net/bbs/read_archive.cgi/anime/11133/1686317062/")
