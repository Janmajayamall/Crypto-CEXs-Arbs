from common_wss import wss_client
import pandas as pd
import json
from websockets_cryptos.constants import ClientResponse, send_it
import websockets_cryptos.constants as constants


class OkexWSS():
    def __init__(self, base_asset, quote_asset):
        self.global_dict={}
        self.stream_url = "wss://real.okex.com:8443/ws/v3"
        self.pair = base_asset+"-"+quote_asset
        self.base_asset = base_asset
        self.quote_asset = quote_asset

    def ticker_handler(self, response):
        response=json.loads(response.decode("utf-8"))
        if "data" in response.keys():
            print("HEre\n", response["data"][0]["best_bid"],response["data"][0]["best_ask"] )
            client_response = ClientResponse(
                                        base_asset=self.base_asset, 
                                        quote_asset=self.quote_asset,
                                        best_bid=response["data"][0]["best_bid"],
                                        bid_quantity=response["data"][0]["base_volume_24h"], #remember the volume is not for the bid. It is for 24_hrs
                                        best_ask=response["data"][0]["best_ask"],
                                        ask_quantity=response["data"][0]["quote_volume_24h"],#remember the volume is not for the bid. It is for 24_hrs
                                        base_asset_alt="",
                                        quote_asset_alt="",
                                        exchange=constants.OKEX
                                    )
            send_it(client_response.get_dict())

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {"op": "subscribe", "args": ["spot/ticker:"+self.pair]}
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_houbiSuscribeTicker", exchange="Okex")
        my_client.start()



# client = OkexWSS("BTC", "USDT")
# client.get_price_quote()


