from common_wss import wss_client
import pandas as pd

class OkexWSS():
    def __init__(self):
        self.global_dict={}
        self.stream_url = "wss://real.okex.com:8443/ws/v3"


    def ticker_handler(self, response):
        print('start')
        print(response)
        print('end')
        pass

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {"op": "subscribe", "args": ["spot/ticker:ETH-USDT"]}
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_houbiSuscribeTicker", exchange="Okex")
        my_client.start()



client = OkexWSS()
client.get_price_quote()


