import uvicorn
import binanceClient
import trader

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    price: str
    symbol: str

app = FastAPI()
globalData = {}

def open(item: Item, type):
    return

@app.on_event("startup")
def init_data():
    print("init call")
    globalData['lastTradeTp'] = True
    globalData['trader'] = trader()
    return globalData

@app.post("/buy")
def buy(item: Item):

    resp = globalData['trader'].buy(symbol="BTCUSDT", price=item.price)
    # TODO: handle resp

    # TODO: STOP on MARK_PRICE and TAKE_PROFIT on CONTRACT_PRICE
    
    globalData['lastTradeTp']=False
    return "buy"

@app.post("/sell")
def sell(item: Item):

    resp = globalData['trader'].sell(symbol="BTCUSDT", price=item.price)
    # TODO: handle resp

    # TODO: STOP on MARK_PRICE and TAKE_PROFIT on CONTRACT_PRICE

    globalData['lastTradeTp']=False
    return resp

@app.post("/tp")
def tp(item: Item):

    resp = globalData['trader'].tp("BTCUSDT")
    # TODO: handle resp

    globalData['lastTradeTp']=True
    return resp
    
if __name__ == '__main__':

    uvicorn.run(app='webhookReceiver:app', host='0.0.0.0', port=8080, reload=True, debug=True)