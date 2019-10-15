from common_wss import wss_client
import pandas as pd

class HoubiWSS():
    def __init__(self):
        self.global_dict={}
        self.stream_url = "wss://api.huobi.pro/ws"


    def ticker_handler(self, response):
        print('start')
        print(response)
        print('end')
        pass

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {"sub": "market.btcusdt.bbo", "id": "id10"}
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_houbiSuscribeTicker", exchange="Houbi")
        my_client.start()



client = HoubiWSS()
client.get_price_quote()


