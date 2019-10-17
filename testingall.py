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


class RunIt():
    def __init__(self, asset_pairs_list, exchange_name):
        print('This', exchange_name, asset_pairs_list)
        self.exchange_name=exchange_name
        self.asset_pairs_list=asset_pairs_list
    def run_it(self):
        if(self.exchange_name==constants.COINBASE):
            for asset_pair in self.asset_pairs_list:
                client = CoinbaseWSS(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()
        if(self.exchange_name==constants.BINANE_EXCHANGE):
            for asset_pair in self.asset_pairs_list:
                client = BinanceWss(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()
        # if(self.exchange_name==constants.DERIBIT):
        #     for asset_pair in self.asset_pairs_list]:
        #         client = DeribitWSS(exchange_dict[exchange]["base_asset"], exchange_dict[exchange]["quote_asset"])
        #         client.get_price_quote()
        if(self.exchange_name==constants.HOUBI):
            for asset_pair in self.asset_pairs_list:
                client = HoubiWSS(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()
        if(self.exchange_name==constants.KRAKEN):
            for asset_pair in self.asset_pairs_list:
                client = KrakenWSS(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()
        if(self.exchange_name==constants.OKEX):
            for asset_pair in self.asset_pairs_list:
                client = OkexWSS(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()
        if(self.exchange_name==constants.BITMEX):
            for asset_pair in self.asset_pairs_list:
                client = BitmexWSS(asset_pair["base_asset"], asset_pair["quote_asset"])
                client.get_price_quote()

exchange_dict = get_asset_pairs()
for exchange in exchange_dict.keys():
    cover = RunIt(exchange_dict[exchange], exchange)
    cover.run_it()

