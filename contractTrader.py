import binanceClient
def contractTrader():
    def __init__(self):
        self.client = binanceClient()

    def sell(symbol, price, quantity=-1, percent=1, tp=True):

        # 首先平仓
        if tp:
            self.tp(symbol)

        if -1 == quantity or 1 == percent:
            # 全部买入

            # 获取账户余额
            balances = self.__client.balance()
            
            # 获取USDT余额
            for balance in balances:
                if "USDT" == balance["asset"]:
                    availableBalance = balance["availableBalance"]
        
        params = {
            'symbol': symbol,
            'side': 'SELL',
            'type': 'LIMIT',
            'quantity': float(availableBalance*0.99)/price,
            'price': price,
            'timeInForce': 'GTC'
        }

        return self.__client.trade(params)

    def buy(symbol, price, quantity=-1, percent=1, tp=True):
        
        # 首先平仓
        if tp:
            self.tp(symbol)

        if -1 == quantity or 1 == percent:
            # 全部买入

            # 获取账户余额
            balances = self.__client.balance()
            
            # 获取USDT余额
            for balance in balances:
                if "USDT" == balance["asset"]:
                    availableBalance = balance["availableBalance"]
        
        params = {
            'symbol': symbol,
            'side': 'BUY',
            'type': 'LIMIT',
            'quantity': float(availableBalance*0.99)/price,
            'price': price,
            'timeInForce': 'GTC'
        }
        
        return self.__client.trade(params)

    def tp(symbol, quantity=-1):
        # symbol: 要平仓的交易对; quantity: 要平仓的数量，-1时为全部平仓

        if -1 == quantity:
            # 根据未平仓数量全部平仓

            # 获取账户信息
            account = self.__client.account()

            # 获取所有头寸
            positions = account["positions"]
            
            for position in positions:
                if position["symbol"] == symbol:
                    # 持仓数量
                    quantity = position["positionAmt"]
                    # 持仓方向
                    positionSide = position["positionSide"]
                    
        # 订单参数
        params = {
            'symbol': symbol,
            #'side': 'SELL',
            'type': 'MARKET',
            'quantity': quantity
        }
    
        # 判断是平多还是平空
        if positionSide == "LONG":
            params['side'] = 'SELL'
        else:
            params['side'] = 'BUY'

        return self.__client.trade(params)