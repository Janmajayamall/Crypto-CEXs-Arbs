from common_wss import wss_client
import pandas as pd

class CoinbaseWSS():
    def __init__(self):
        self.global_dict={}
        self.stream_url = 'wss://ws-feed.pro.coinbase.com'

    def ticker_handler(self, response):
        print('start')
        print(response)

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "type": "subscribe",
            "product_ids": [
                "BTC-USD",
            ],
            "channels": [
                "heartbeat",
                "ticker"
            ]
        }
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_coinbaseSuscribeTicker")
        my_client.start()


bitmex_wss = CoinbaseWSS()
bitmex_wss.get_price_quote()