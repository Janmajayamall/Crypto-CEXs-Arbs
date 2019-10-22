from common_wss import wss_client
import pandas as pd
from websockets_cryptos.constants import ClientResponse, send_it
import json
import websockets_cryptos.constants as constants


class HoubiWSS():
    def __init__(self, base_asset, quote_asset, callback_func):
        self.global_dict={}
        self.stream_url = "wss://api.huobi.pro/ws"
        self.pair = base_asset.lower()+quote_asset.lower()
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.callback_func = callback_func

    def ticker_handler(self, response):
        response=json.loads(response)
        if "ch" in response.keys():
            client_response = ClientResponse(
                                                base_asset=self.base_asset, 
                                                quote_asset=self.quote_asset,
                                                best_bid=response["tick"]["bid"],
                                                bid_quantity=response["tick"]["bidSize"],
                                                best_ask=response["tick"]["ask"],
                                                ask_quantity=response["tick"]["askSize"],
                                                base_asset_alt="",
                                                quote_asset_alt="",
                                                exchange=constants.HOUBI
                                            )
            self.callback_func.channel_publish(client_response.get_dict())



    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {"sub": "market."+self.pair+".bbo", "id": self.pair+"_houbi_price_quote"}
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_houbiSuscribeTicker", exchange="Houbi")
        my_client.start()



# client = HoubiWSS("LTC", "BTC", send_it)
# client.get_price_quote()


