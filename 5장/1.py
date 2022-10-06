import requests
from bs4 import BeautifulSoup

title=input("제목")
index1=input("내용")
requeste=requests.post(
    "https://controlc.com/index.php",
    params={
        "act": "submit"
    },
    data={
        "subdomain" :"", 
        "antispam": "1",
        "website": "",
        "paste_title": title,
        "input_text": index1,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": "",
        "code": "0",
    },
    headers={
        "referer": "https://controlc.com/"
    }

)


soup=BeautifulSoup(requeste.text,'html.parser')
url=soup.select_one(".input-copy>form>input")
your_new_url= url.attrs["value"]

requeste2=requests.get(
    your_new_url
)
soup2=BeautifulSoup(requeste2.text,'html.parser')
title=soup2.select_one(".whiteBG>div:nth-child(2)")


print("당신의 메모 url은",your_new_url,"입니다")
print("당신의 메모제목은",title.text,"입니다")