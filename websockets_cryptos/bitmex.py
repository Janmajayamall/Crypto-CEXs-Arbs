from common_wss import wss_client
import pandas as pd
from websockets_cryptos.constants import ClientResponse, send_it
from websockets_cryptos import constants

class BitmexWSS():
    def __init__(self, base_asset, quote_asset):
        self.global_dict={}
        self.stream_url = 'wss://www.bitmex.com/realtime'
        self.pair = base_asset+quote_asset
        self.base_asset = base_asset
        self.quote_asset = quote_asset,


    def ticker_handler(self, response):
        if "data" in response.keys():
            client_response = ClientResponse(
                                                base_asset=self.base_asset, 
                                                quote_asset=self.quote_asset,
                                                best_bid=response["data"][0]["bidPrice"],
                                                bid_quantity=response["data"][0]["bidSize"],
                                                best_ask=response["data"][0]["askPrice"],
                                                ask_quantity=response["data"][0]["askSize"],
                                                base_asset_alt="",
                                                quote_asset_alt="",
                                                exchange=constants.BITMEX
                                            )            
            send_it(client_response.get_dict())

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "op": "subscribe",
            "args": ["quote:"+self.pair],
        }
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_krakenSuscribeBook")
        my_client.start()


# client = BitmexWSS("XBT", "USD")
# client.get_price_quote()


