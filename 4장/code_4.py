from cgitb import html
from turtle import title
from bs4 import BeautifulSoup
import requests

with open ("./4장/test.html","r",encoding="utf-8")as f: 
    html = f.read() 

soup = BeautifulSoup(html, "html.parser") 
a = soup.select_one(".input-copy input") 

# print(a.attrs["value"]) ## 속성 값을 딕셔너리로 받아오고 키로 value를 사용해서 추출     

                                        

# response = requests.post( 
#     a.attrs["value"],
#     headers={
#         "referer" : "https://controlc.com/61e530ab"
#     }
# )

# with open("./c.html","w",encoding="utf-8") as f:
#     f.write(response.text)

# with open ("./4장/c.html","r",encoding="utf-8")as f: 
#     html = f.read() 

# soup = BeautifulSoup(html, "html.parser") 
# b = soup.select_one("#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)") 
# print(b.get_text())


response1 = requests.get("https://controlc.com/61e530ab")
soup1 = BeautifulSoup(response1.text , "html.parser")
c = soup1.select_one("#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)")
print(c.get_text())
