import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time
    
datas = []

for page in range(1,120): 
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
        "total": "1379",
        "block": page,
        "start": "",
        "next": "",
        "addr1": "서울",
        "addr2": "",
        "addr3": "",
        "bubcd": "" ,
        "kye": "",
        "local_num": "",
        "var_period": "" ,
        "result": "99",
        "var_kind": "",
        "yuchalcnt": "",
        "gamprice": "",
        "lowprice": "" ,
        "bdarea": "",
        "daejiarea": "",
        "ipchaltype": "", 
        "bdname": "",
        "special": "",
        "addshow": "",
        "sort": "13D",
        "subMenuIdx": "1",
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Whale/3.16.138.27 Safari/537.36",
        "Origin": "https://auction.realestate.daum.net",
        "Referer": "https://auction.realestate.daum.net/v15/"
    }
)
    
    soup1 = BeautifulSoup(requests1.text,"html.parser")
    trs = soup1.select("#frm_myreg > table > tbody > tr")
    print("페이지",page,"tr개수",len(trs))
    
    if len(trs) == []:
        print(f"{page}에서 종료")
        break

    for i in trs:
        data = {
            "사건번호" : i.select_one("td:nth-child(1) a").text,
            "물건용도" : i.select_one(".used").text,
            "주소" : i.select_one(".address").text,
            "가격" : i.select_one(".posotion").text
        }

        datas.append(data)
        time.sleep(5) # 서버에게 비정상적인 요청으로 감지되지 않게 5초 쉬기
        
with open("./7장/"+"1~116"+".json","w",encoding="utf-8")as f:
    f.write(json.dumps(datas,ensure_ascii=False)) 
        



    
    