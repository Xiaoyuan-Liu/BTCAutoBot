from binance.futures import Futures

import json

def binanceClient():
    def __init__(self):
        with open("ApiKeyConfig.json", 'r') as fp:
            apiDict = json.load(fp)
        
        self.__apiKey = apiDict["apiKey"]
        self.__secretKey = apiDict["secretKey"]
        self.__client = Futures(key=self.__apiKey, secret=self.secretKey)

    def __contractSell():
        return

    def __contractBuy():
        return

    def __USDTSell():
        return

    def __USDTBuy():
        return

    def trade(params): 
        
        #params = {
            # '参数名称': 参数值 # 参数类型， 是否必须参数， 描述
            #'symbol': symbol, # STRING, YES, 交易对
            #'side': side, # ENUM, YES, 买卖方向 SELL, BUY
            #'positionSide': None, # ENUM, NO, 持仓方向, 单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT
            #'type': type, # ENUM, YES, 订单类型 LIMIT(限价单), MARKET(市价单), STOP(止损限价单), TAKE_PROFIT(止盈限价单), STOP_MARKET(止损市价单), TAKE_PROFIT_MARKET(止盈市价单), TRAILING_STOP_MARKET(跟踪止损单)
            #'reduceOnly': None, # STRING, NO, true, false; 非双开模式下默认false；双开模式下不接受此参数； 使用closePosition不支持此参数。
            #'quantity': quantity, # DECIMAL, NO, 下单数量,使用closePosition不支持此参数。
            #'price': 59808, # DECIMAL, NO, 委托价格
            #'newClientORderId': None, # STRING, NO, 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 ^[\.A-Z\:/a-z0-9_-]{1,36}$
            #'stopPrice': None, # DECIMAL, NO, 触发价, 仅 STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET 需要此参数
            #'closePosition': None, # STRING, NO, true, false；触发后全部平仓，仅支持STOP_MARKET和TAKE_PROFIT_MARKET；不与quantity合用；自带只平仓效果，不与reduceOnly 合用
            #'activationPrice': None, # DECIMAL, NO, 追踪止损激活价格，仅TRAILING_STOP_MARKET 需要此参数, 默认为下单当前市场价格(支持不同workingType)
            #'callbackRate': None, # DECIMAL, NO, 追踪止损回调比例，可取值范围[0.1, 5],其中 1代表1% ,仅TRAILING_STOP_MARKET 需要此参数
            #'timeInForce': 'GTC', # ENUM, NO, 有效方法
            #'workingType': None, # ENUM, NO, stopPrice 触发类型: MARK_PRICE(标记价格), CONTRACT_PRICE(合约最新价). 默认 CONTRACT_PRICE
            #'priceProtect': None, # STRING, NO, 条件单触发保护："TRUE","FALSE", 默认"FALSE". 仅 STOP, STOP_MARKET, TAKE_PROFIT, TAKE_PROFIT_MARKET 需要此参数
            #'newOrderRespType': None, # ENUM, NO, "ACK", "RESULT", 默认 "ACK"
            #'recvWindow': None, # LONG, NO
            #'timestamp': None #LONG, No
        #}
        # 根据type的不同，某些参数强制要求
        # LIMIT: timeInForce, quantity, price
        # MARKET: quantity
        # STOP, TAKE_PROFIT: quantity, price, stopPrice
        # STOP_MARKET, TAKE_PROFIT_MARKET: stopPrice
        # TRAILING_STOP_MARKET: callbackRate

        return self.__client.new_order_test(**params)

    def position(symbol):
        account = self.__client.account()
        positionList = account["positions"]
        for position in positionList:
            if position['symbol'] == symbol:
                return position
        return
    
    def balance(asset):
        balances = self.__client.balance()
        for balance in balances:
            if balance['asset'] == asset:
                return balance
        return