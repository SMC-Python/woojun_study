import requests

## 값을 입력받아서 title과 content에 저장
title = input("제목을 입력하세요 : ")
content = input("제목을 입력하세요 : ")

response = requests.post( 
    "https://controlc.com/index.php",
    params={ # 개발자 모드 페이로드 안에 act: submit을 가져옴
        "act": "submit",
    },
    data={ # 개발자 모드 페이로드 안에 양식데이터를 가져옴 / 메모에 제목과 내용을 결정하는 paste_title 과 input_text를 입력받는 값들로 변경한다
        "subdomain" : "",
        "antispam": "1",
        "website" : "" ,
        "paste_title" : title,
        "input_text" : content,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": "",
        "code" : "0",
    },
    headers={ ## 개발자 모드에 요청 헤더 부분을 가져와줌 / 이사이트는 referer만 있으면 정상적 요청으로 인식
        # "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.87 Whale/3.16.138.22 Safari/537.36",
        # "origin" : "https://controlc.com",
        "referer" : "https://controlc.com/"
    }
)
# 저장 방법 open 뒤에 저장할 주소와 이름을 적는다
with open("/Users/woojun/Documents/One_team_one_company_class-source_code/test.html",
"w",
encoding="utf-8") as f:
    f.write(response.text)
