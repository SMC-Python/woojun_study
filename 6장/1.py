import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

requests1 = requests.post(
    "https://auction.realestate.daum.net/ajax/main_list.php",
    params={
        "addr1": "서울",
        "result": "99",
        "yongdo": "99",
        "yongdo_detail": "99",
        "sort": "13D"
    },
    data={
        "total": "1304",
        "block": "1",
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
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36",
        "Origin": "https://auction.realestate.daum.net",
        "Referer": "https://auction.realestate.daum.net/v15/"
    }
)
with open("./6장/1.html","w",encoding="utf-8")as f:
    f.write(requests1.text)
soup1 = BeautifulSoup(requests1.text,"html.parser")
trs = soup1.select("#frm_myreg > table > tbody > tr")

datas = []

for i in trs:
    data = {
        "사건번호" : i.select_one("td:nth-child(1) a").text,
        "물건용도" : i.select_one(".used").text,
        "주소" : i.select_one(".address").text,
        "가격" : i.select_one(".posotion").text
    }
    # print("")
    # print("사건번호 :",i.select_one("td:nth-child(1) a").text)
    # print("물건용도 :",i.select_one(".used").text)
    # print("주소 :",i.select_one(".address").text)
    # print("가격 :",i.select_one(".posotion").text)
    # print("_"*50)
    
    datas.append(data)
    
    with open("./6장/2.json","w",encoding="utf-8")as f:
        f.write(json.dumps(datas,ensure_ascii=False)) # list형인 data를 string으로 변환하여 json으로 변환 
    
    # pprint(data)
    
    # pprint(datas)
    
    