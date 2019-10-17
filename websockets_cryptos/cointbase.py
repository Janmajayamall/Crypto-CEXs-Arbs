from common_wss import wss_client
import pandas as pd
from  websockets_cryptos.constants import ClientResponse, send_it
from websockets_cryptos import constants


class CoinbaseWSS():
    def __init__(self, base_asset, quote_asset):
        self.global_dict={}
        self.stream_url = 'wss://ws-feed.pro.coinbase.com'
        self.pair = base_asset+"-"+quote_asset
        self.base_asset = base_asset
        self.quote_asset = quote_asset

    def ticker_handler(self, response):
        if response["type"]=="ticker":
            client_response = ClientResponse(
                                                base_asset=self.base_asset, 
                                                quote_asset=self.quote_asset,
                                                best_bid=response["best_bid"],
                                                bid_quantity="",
                                                best_ask=response["best_ask"],
                                                ask_quantity="",
                                                base_asset_alt="",
                                                quote_asset_alt="",
                                                exchange=constants.COINBASE
                                            )
            send_it(client_response.get_dict())

    def get_price_quote(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "type": "subscribe",
            "product_ids": [
                self.pair
            ],
            "channels": [
                "ticker"
            ]
        }
        my_client.subscribe_public(payload, callback=self.ticker_handler,id_="_coinbaseSuscribeTicker")
        my_client.start()


# bitmex_wss = CoinbaseWSS('BAT', 'USDC')
# bitmex_wss.get_price_quote()