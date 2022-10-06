from cgitb import html
from turtle import title
from bs4 import BeautifulSoup

with open ("./4장/4-2.html","r",encoding="utf-8")as f: 
    html = f.read() 

soup = BeautifulSoup(html, "html.parser") 
li_list = soup.select("#content-box > ul > li") 

for i in li_list:
    print(i.get_text())