#format of obj response to client
class ClientResponse():
    def __init__(self, base_asset, quote_asset, best_bid, bid_quantity, best_ask, ask_quantity, base_asset_alt, quote_asset_alt, exchange):
        self.base_asset=base_asset
        self.quote_asset=quote_asset
        self.best_bid=best_bid
        self.bid_quantity=bid_quantity
        self.best_ask=best_ask
        self.ask_quantity=ask_quantity
        self.base_asset_alt=base_asset_alt
        self.quote_asset_alt=quote_asset_alt,
        self.exchange=exchange
    
    def get_dict(self):
        return({
                    "base_asset" : self.base_asset,
                    "quote_asset" : self.quote_asset,
                    "best_bid" : self.best_bid,
                    "bid_quantity" : self.bid_quantity,
                    "best_ask" : self.best_ask,
                    "ask_quantity" : self.ask_quantity,
                    "base_asset_alt": self.base_asset_alt,
                    "quote_asset_alt": self.quote_asset_alt,
                    "exchange":self.exchange
                })


#format of asset pairs
class CurrencyFormat():
    def __init__(self, base_asset=None, base_asset_alt=None, quote_asset=None, quote_asset_alt=None):
        self.base_asset = base_asset
        self.base_asset_alt = base_asset_alt
        self.quote_asset = quote_asset
        self.quote_asset_alt = quote_asset_alt
    
    def get_dict(self):
        return({
                    "base_asset":self.base_asset,
                    "base_asset_alt":self.base_asset_alt,
                    "quote_asset":self.quote_asset,
                    "quote_asset_alt":self.quote_asset_alt
                })



COINBASE = "COINBASE"
BINANE_EXCHANGE = "BINANCE_EXCHANGE"
DERIBIT = "DERIBIT"
HOUBI = "HOUBI"
KRAKEN = "KRAKEN"
OKEX = "OKEX"
BITMEX = "BITMEX"



def send_it(response):
    print('got it\n', response)



