import time
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
datas = []
for page in range(1,151):
    response=requests.post(
        'https://auction.realestate.daum.net/ajax/main_list.php',
        params={
            'addr1': '서울',
            'result': '99',
            'yongdo': '99',
            'yongdo_detail': '99',
            'sort': '13D'
        },
        data={
            'total': '1379',
            'block': page,
            'start': '',
            'next': '',
            'addr1': '서울',
            'addr2': '',
            'addr3': '',
            'bubcd': '',
            'kye': '',
            'local_num': '',
            'var_period': '',
            'result': '99',
            'var_kind': '',
            'yuchalcnt': '',
            'gamprice': '',
            'lowprice': '',
            'bdarea': '',
            'daejiarea': '',
            'ipchaltype': '',
            'bdname': '',
            'special': '',
            'addshow': '',
            'sort': '13D',
            'subMenuIdx': '1'
        },
        headers={
            'Origin': 'https://auction.realestate.daum.net',
            'Referer': 'https://auction.realestate.daum.net/v15/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    trs = soup.select('#frm_myreg > table > tbody> tr')
    print('페이지:', page, 'tr 개수:', len(trs))
    if len(trs) == 0:
        print(f"{page}부터 빈 페이지 입니다.") #문자열 앞에 'f'를 적으면 문자열 안에서 괄호를 넣고 변수를 넣을 수 있음
        break
    for tr in trs:
        data={
            '사건번호' : tr.select_one('td:nth-child(1) a').get_text(),
            '물건용도' : tr.select_one('.used').get_text(),
            '소재지' : tr.select_one('.address').get_text(),
            '면적': tr.select_one('.area > span').get_text(),
            '감정가': tr.select_one('td:nth-child(3) > div:nth-child(1) > p:nth-child(1)').get_text(),
        }
        datas.append(data)
    time.sleep(5)#시간 지연-사이트에서는 연속적으로 크롤링을 하게되면 비정상적 사용자로 분류하여 차단을 시킴으로 시간 지연을 넣음으로써 차단을 방지함
with open('./code_1.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(datas, ensure_ascii=False))