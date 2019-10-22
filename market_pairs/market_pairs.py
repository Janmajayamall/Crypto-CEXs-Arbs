'''
Script to get list of all cryptocurrencies
'''

import requests
import json
import websockets_cryptos.constants as constants
import copy



class GetCurrencies():

    '''
    Declaring apis and their respective self.ENDPOINTS
    '''
    def __init__(self):
        self.ENDPOINTS ={
            constants.BINANE_EXCHANGE :"https://api.binance.com/api/v1/exchangeInfo",
            constants.COINBASE : "https://api-public.sandbox.pro.coinbase.com",
            constants.DERIBIT : "",
            constants.OKEX : "",
            constants.HOUBI : "https://api.huobi.com/v1/common/symbols",
            constants.KRAKEN : "https://api.kraken.com/0/public/Assets",
            constants.BITMEX : ""
        }

    def coinbase(self):
        all_currencies = []
        response = requests.get(self.ENDPOINTS[constants.COINBASE] + '/products')
        response=response.json()
        for i in response:
            temp_currency = constants.CurrencyFormat(
                                                        base_asset=i['id'].split('-')[0],
                                                        base_asset_alt="",
                                                        quote_asset=i['id'].split('-')[1],
                                                        quote_asset_alt=""
                                                    )
            all_currencies.append(temp_currency.get_dict())
        return all_currencies

    def kraken(self):
        all_currencies = []
        response = requests.get(self.ENDPOINTS[constants.KRAKEN])
        response=response.json()
        if response['error'] != []:
            print('kraken error; not able to get its currency list')
        else:
            for i in response['result'].keys():
                for j in response['result'].keys():
                    if i!=j:
                        temp_currency = constants.CurrencyFormat(
                                            base_asset=response['result'][i]['altname'],
                                            base_asset_alt=i,
                                            quote_asset=response['result'][j]['altname'],
                                            quote_asset_alt=j
                                        )
                        all_currencies.append(temp_currency.get_dict())
        return all_currencies
    
    def houbi(self):
        all_currencies = []
        response = requests.get(self.ENDPOINTS[constants.HOUBI])
        response=response.json()
        if response['status'] != 'ok':
            print('HOUBI error; not able to get its currency list')
        else:
            for i in response['data']:
                temp_currency = constants.CurrencyFormat(
                                            base_asset=i['base-currency'],
                                            base_asset_alt="",
                                            quote_asset=i['quote-currency'],
                                            quote_asset_alt=""
                                        )
                all_currencies.append(temp_currency.get_dict())
        return all_currencies

    def binance_exchange(self):
        all_currencies = []
        response = requests.get(self.ENDPOINTS[constants.BINANE_EXCHANGE])
        response=response.json()
        for i in response['symbols']:
            temp_currency = constants.CurrencyFormat(
                                            base_asset=i['baseAsset'],
                                            base_asset_alt="",
                                            quote_asset=i['quoteAsset'],
                                            quote_asset_alt=""
                                        )
            all_currencies.append(temp_currency.get_dict())
        return all_currencies 

    def deribit(self):
        return[]  

    def okex(self):
        return[]

    def bitmex(self):
        all_currencies=[]
        #manualy returning XBT/USD
        temp_currency = constants.CurrencyFormat(
                                                    base_asset="XBT",
                                                    base_asset_alt="",
                                                    quote_asset="USD",
                                                    quote_asset_alt=""
                                                )
        all_currencies.append(temp_currency.get_dict())
        return all_currencies



def get_asset_pairs():
    client = GetCurrencies()

    # dictionary of asset pairs
    return({
        constants.BINANE_EXCHANGE:client.binance_exchange(),
        constants.COINBASE:client.coinbase(),
        constants.DERIBIT:client.deribit(),
        constants.KRAKEN:client.kraken(),
        constants.HOUBI:client.houbi(),
        constants.OKEX:client.okex(),
        constants.BITMEX:client.bitmex()
    })
