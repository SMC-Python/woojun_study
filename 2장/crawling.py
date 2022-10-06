import requests

# https://search.naver.com/search.naver

# ?where=nexearch
# &sm=top_hty
# &fbm=1
# &ie=utf8
# &query=가나다

response = requests.get(
    "https://search.naver.com/search.naver",
    params={
        "where" : "nexearch",
        "sm" : "top_hty",
        "fbm" : "1",
        "ie" : "utf8",
        "query" : "가나다"
    }
)


# print(response.status_code)
# print(response.text) 

#https://dict.naver.com/search.dict?dicQuery=test&query=test&target=dic&ie=utf8&query_utf=&isOnlyViewEE=

# https://dict.naver.com/search.dict
# ?dicQuery=test
# &query=test
# &target=dic
# &ie=utf8
# &query_utf=
# &isOnlyViewEE=

response1 = requests.get(
    "https://dict.naver.com/search.dict",
    params={
        "dicQuery" : "test",
        "query" : "test",
        "target" : "dic",
        "ie" : "utf8",
        "query_utf" : " ",
        "isOnlyViewEE" : " "
    }
)

print(response1.text) 

# open 바로 앞에 적힌 것이 파일 경로
# w는 writing 하는 용도
# "f라는 객체를 통해 접근"

with open("C:/Users/user/Desktop/crawling/crawling.html","w",encoding="utf-8") as f:
    f.write(response1.text)