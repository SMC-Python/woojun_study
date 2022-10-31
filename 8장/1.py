

from fastapi import FastAPI

app = FastAPI()

# 주소(경로)
@app.get('/hello') #행위 / 자원
def hello():
    return {'text': 'hello'}#딕셔너리 타입 / # 표현
#주소창에 localhost와 터미널에 'uvicorn "파일명":app --reload'를 
# 치면 나오는 주소의 :뒷 번호 를 붙인 후 위의 주소를 적음 ex)http://localhost:8000/hello

@app.get('/users')
def get_users(username: str):
    return {'username': username}

@app.post('/users')
def create_users(username: str):
    return {'username': username}

@app.get('/users/{username}')
def get_users(username: str):
    return {'username': username}