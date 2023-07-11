import sys

import requests
from bs4 import BeautifulSoup

import db_input


def thread_input(load_url):
    """
    スレのURLを読み込んで全ての日付とコメントを返す
    """

    # Webページを取得して解析する
    html = requests.get(load_url)#URLを読み込む
    soup = BeautifulSoup(html.content, "html.parser")
    
    
    try:
        for num in range(1,3002):#コメント読み込む
            element = soup.find(id="comment_" + str(num))    # その中のliタグの文字列を表示
            
            text = element.get_text(strip=True)# テキストを抽出
            extracted_text = text.split('：')[2]
            print(extracted_text[0:13])#日付
            print(extracted_text[14:22])    
            next_tag = element.find_next_sibling()#日付の下のコメント抽出
            print(next_tag.text)#コメント
            print("coment input date!!")
            #DBに入れる
            db_input.db_input(extracted_text[0:13],extracted_text[14:22],next_tag.text)
            
            
    
    except AttributeError:#不明な行を読み込んだ際
        print("None...")
        sys.exit()  # 処理を終了する
    
    

def date_get():
    """
    タグの要素を取得して３つ目の
    """
    
    return 0

thread_input("https://jbbs.shitaraba.net/bbs/read_archive.cgi/anime/11133/1686317062/")
