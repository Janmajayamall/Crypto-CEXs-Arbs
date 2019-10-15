from common_wss import wss_client
import pandas as pd

class BitmexWSS():
    def __init__(self):
        self.global_dict={}
        self.stream_url = 'wss://www.bitmex.com/realtime'

    def ticker_handler(self, response):
        print('start')
        print(response)

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "op": "subscribe",
            "args": ["quote:XBTUSD"],
        }
        my_client.subscribe_public(payload, callback=self.my_handler,id_="_krakenSuscribeBook")
        my_client.start()


bitmex_wss = BitmexWSS()
bitmex_wss.generate_order_book()