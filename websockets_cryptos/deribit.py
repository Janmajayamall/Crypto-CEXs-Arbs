# from common_wss import wss_client
# import pandas as pd

# class DeribitWSS():
#     def __init__(self):
#         self.global_dict={}
#         self.stream_url = 'wss://testapp.deribit.com/ws/api/v2'

#     def ticker_handler(self, response):
#         print('start')
#         print(response)

#     def get_price_quote(self):
#         my_client = wss_client.WssClient(self.stream_url)
#         payload = {"jsonrpc": "2.0",
#                     "method": "public/subscribe",
#                     "params": {
#                         "channels": ["quote.BTC-PERPETUAL", "quote.BTC-USD"]}
#                     }
#         my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_deribitSuscribeTicker")
#         my_client.start()


# # deribitWss = DeribitWSS()
# # deribitWss.get_price_quote()