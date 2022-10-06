from tkinter import W
import requests
from bs4 import BeautifulSoup

requests1=requests.post(
    "https://auction.realestate.daum.net/ajax/main_list.php",
    params={
        "addr1": "서울",
        "result": "99",
        "yongdo": "99",
        "yongdo_detail": "99",
        "sort": "13D"
    },
    data={
        "total": "1293",
        "block": "3",
        "start": "",
        "next": "",
        "addr1": "서울",
        "addr2": "",
        "addr3": "",
        "bubcd": "",
        "kye": "",
        "local_num": "",
        "var_period": "",
        "result": "99",
        "var_kind": "",
        "yuchalcnt": "",
        "gamprice": "",
        "lowprice": "",
        "bdarea": "",
        "daejiarea": "",
        "ipchaltype": "",
        "bdname": "",
        "special": "",
        "addshow": "",
        "sort": "13D",
        "subMenuIdx": "1"
    },
    headers={
        "Host": "auction.realestate.daum.net",
        "Origin": "https://auction.realestate.daum.net",
        "Referer": "https://auction.realestate.daum.net/v15/"
    }
)
#html 파일 제작 국내 사이트 일부는 euc-kr로 인코딩 해야한다
# with open("/Users/woojun/Documents/One_team_one_company_class-source_code/5장/code_2.html","w",encoding="utf-8") as f:
#     f.write(requests1.text)
soup = BeautifulSoup(requests1.text,"html.parser")
trs = soup.select("#frm_myreg > table > tbody > tr")
for i in trs:
    print(i.select_one("td:nth-child(1) a").text)
# 크롬에서는 보정을 해주기 때문에 html 파일이 실제와 다를 수 있으니 주의