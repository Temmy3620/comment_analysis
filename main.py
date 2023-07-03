import requests
from bs4 import BeautifulSoup


# Webページを取得して解析する

load_url = "https://jbbs.shitaraba.net/bbs/subject.cgi/anime/11133/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")



# aタグを解析データから特定のID内から全て見つけてhref属性の中身を表示
related = soup.find(class_="thread-list")

#print(related)


# 指定したIDの中からaタグを探してhrefをプリント
for element in related.find_all("a"):
    url = element.get("href")
    print(url)

