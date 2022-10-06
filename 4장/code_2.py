from cgitb import html
from turtle import title
from bs4 import BeautifulSoup

with open ("./4장/4-1.html","r",encoding="utf-8")as f: # r은 파일을 열어서 읽는다는 의미 f라는 변수를 통해 접근하겠다
    html = f.read() # 읽은 내용을 html이라는 변수에 넣겠다

soup = BeautifulSoup(html, "html.parser") #BeautifulSoup객체를 soup에 담는다
title1 = soup.select_one("#title") #하나만 찾을땐 select_one 여러개는 select / title1이라는 변수에 담는다

print(title1.get_text()) # get_text로 내용만 추출