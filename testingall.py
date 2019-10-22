from market_pairs.market_pairs import GetCurrencies, get_asset_pairs
import websockets_cryptos.constants as constants
from websockets_cryptos.binance_exchange import BinanceWss
from websockets_cryptos.bitmex import BitmexWSS
from websockets_cryptos.cointbase import CoinbaseWSS
# from websockets_cryptos.deribit import DeribitWSS
from websockets_cryptos.houbi import HoubiWSS
from websockets_cryptos.okex import OkexWSS
from websockets_cryptos.kraken import KrakenWSS
from time import sleep

#importing stuff for websockets
import pika
import sys
import json


class RunIt():
    def __init__(self, asset_pairs_list, exchange_name, update_client):
        self.exchange_name=exchange_name
        self.asset_pairs_list=asset_pairs_list
        self.update_client = update_client
        
    def run_it(self):
        if(self.exchange_name==constants.COINBASE):
            for asset_pair in self.asset_pairs_list:
                client = CoinbaseWSS(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
                client.get_price_quote()
        # if(self.exchange_name==constants.BINANE_EXCHANGE):
        #     for asset_pair in self.asset_pairs_list:
        #         client = BinanceWss(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
        #         client.get_price_quote()
        if(self.exchange_name==constants.DERIBIT):
            for asset_pair in self.asset_pairs_list:
                client = DeribitWSS(exchange_dict[exchange]["base_asset"], exchange_dict[exchange]["quote_asset"])
                client.get_price_quote()
        if(self.exchange_name==constants.HOUBI):
            for asset_pair in self.asset_pairs_list:
                client = HoubiWSS(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
                client.get_price_quote()
        if(self.exchange_name==constants.KRAKEN):
            for asset_pair in self.asset_pairs_list:
                client = KrakenWSS(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
                client.get_price_quote()
        if(self.exchange_name==constants.OKEX):
            for asset_pair in self.asset_pairs_list:
                client = OkexWSS(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
                client.get_price_quote()
        if(self.exchange_name==constants.BITMEX):
            for asset_pair in self.asset_pairs_list:
                client = BitmexWSS(asset_pair["base_asset"], asset_pair["quote_asset"], self.update_client)
                client.get_price_quote()


class PikaAMQP():

    def __init__(self):
        self.connection = pika.BlockingConnection(
                                pika.ConnectionParameters(host="localhost")
                            )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange="quote_updates", exchange_type="fanout")

    def channel_publish(self,response):
        response = json.dumps(response)
        self.channel.basic_publish(exchange="quote_updates", routing_key="", body=response)

 
if __name__ == "__main__":

    update_client = PikaAMQP()

    exchange_dict = get_asset_pairs()

    for exchange in exchange_dict.keys():
        cover = RunIt(exchange_dict[exchange], exchange, update_client)
        cover.run_it()


    # connection.close()






