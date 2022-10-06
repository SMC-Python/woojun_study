import requests

t = input("제목을 입력하세요")
c = input("내용을 입력하세요")

response = requests.post( 
    "https://controlc.com/index.php",
    params={ 
        "act": "submit",
    },
    data={ 
        "subdomain" : "",
        "antispam": "1",
        "website" : "" ,
        "paste_title" : t,
        "input_text" : c,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": "",
        "code" : "0",
    },
    headers={
        "referer" : "https://controlc.com/"
    }
)

with open("./test.html","w",encoding="utf-8") as f:
    f.write(response.text)
