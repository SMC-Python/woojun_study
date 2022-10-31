from importlib.resources import path
import json
from fastapi import FastAPI,HTTPException,Path

app = FastAPI()

def _get_actions() -> list:
    # auctions.json의 내용을 반환
    with open('./auctions.json','r',encoding='utf-8')as f:
        return json.loads(f.read())

def _save_actions(auction:list):
    # auctions 인자를 받아 acutions.json에 저장
    with open('./auctions.json','w',encoding='utf-8')as f:
        f.write(json.dumps(auction,ensure_ascii=False))
        
        
if __name__ == '__main__':
    print(_get_actions())
        
        
# 1. 경매 목록 가져오기
# 2. 경매 목록 중 두 번째 경매 가져오기
# 3. 경매 목록 중 두 번째 경매 삭제하기

@app.get('/')
def ok():
    return {'status' : 'ok'}

@app.get('/auctions')
def get_auctions():
    return _get_actions()

@app.get('/auctions/{id}')
def get_auction(id:int = Path(gt=0)):
    try:
        return _get_actions()[id-1]
    except IndexError:
        raise HTTPException(404)
    
@app.delete('/auctions/{id}')
def delete_auction(id:int = Path(gt=0)):
    a = _get_actions()
    a.pop(id-1)
    try:
        return _save_actions(a)
    except IndexError:
        raise HTTPException(404)