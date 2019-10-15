from binance.client import Client
from binance.websockets import BinanceSocketManager

class BinanceWss():

    def __init__(self):
        '''
        Reference:
            Please use @https://python-binance.readthedocs.io/en/latest/websockets.html for further API reference
        '''
        self.API_KEY = 'EvDVICOk4YXmJ5q9Pxp6NVrPGdcSwIGMSiOozfjed2gzoLIT8qMBnLdEiadgmtRS'
        self.API_SECRET = 'scspaU9SFo9TCormsZjqX9Uldngtv6xOGkVjClBDiHW6II0HwKBzfjiobIXBZEk4'
        self.client = Client(self.API_KEY, self.API_SECRET)
        self.binance_socket_manager = BinanceSocketManager(self.client)

    def ticker_handler(self, response):
        print(response)

    def get_price_quote(self):
        conn = self.binance_socket_manager.start_ticker_socket(self.ticker_handler)
        self.binance_socket_manager.start()


binance_wss = BinanceWss()
binance_wss.get_price_quote()