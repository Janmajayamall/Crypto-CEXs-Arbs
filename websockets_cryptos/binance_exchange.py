from binance.client import Client
from binance.websockets import BinanceSocketManager
from websockets_cryptos.constants import ClientResponse,send_it
import copy
import websockets_cryptos.constants as constants
class BinanceWss():

    def __init__(self, base_asset, quote_asset, callback_func):
        '''
        Reference:
            Please use @https://python-binance.readthedocs.io/en/latest/websockets.html for further API reference
        '''
        self.API_KEY = 'EvDVICOk4YXmJ5q9Pxp6NVrPGdcSwIGMSiOozfjed2gzoLIT8qMBnLdEiadgmtRS'
        self.API_SECRET = 'scspaU9SFo9TCormsZjqX9Uldngtv6xOGkVjClBDiHW6II0HwKBzfjiobIXBZEk4'
        self.client = Client(self.API_KEY, self.API_SECRET)
        self.binance_socket_manager = BinanceSocketManager(self.client)
        self.pair = base_asset+quote_asset
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.callback_func = callback_func

    def ticker_handler(self, response):
        client_response = ClientResponse(
                                            base_asset=self.base_asset, 
                                            quote_asset=self.quote_asset,
                                            best_bid=response["b"],
                                            bid_quantity=response["B"],
                                            best_ask=response["a"],
                                            ask_quantity=response["A"],
                                            base_asset_alt="",
                                            quote_asset_alt="",
                                            exchange=constants.BINANE_EXCHANGE
                                         )
        self.callback_func.channel_publish(client_response.get_dict())

    def get_price_quote(self):
        conn = self.binance_socket_manager.start_symbol_ticker_socket(self.pair,self.ticker_handler)
        self.binance_socket_manager.start()

# clinet=BinanceWss("IOTA", "BTC", send_it )
# clinet.get_price_quote()