from cgitb import html
from html.parser import HTMLParser
from turtle import tilt
from urllib import response
import requests
from bs4 import BeautifulSoup

title = input("제목")
content = input("내용") 

requests1=requests.post(
"https://controlc.com/index.php",
    params={
        "act": "submit"
    },
    data={
        "subdomain":"" ,
        "antispam": "1",
        "website": "",
        "paste_title": title,
        "input_text": content,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": "",
        "code": "0",
    },
    headers={
        "referer": "https://controlc.com/"
    }
)

soup1 = BeautifulSoup(requests1.text,'html.parser')
url=soup1.select_one(".input-copy>form>input")
url = url.attrs["value"]
print("주소는"+url)

response2 = requests.get (url)
soup2 = BeautifulSoup(response2.text,'html.parser')
title = soup2.select_one("#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)")
title = title.get_text()

print("제목은"+title)
