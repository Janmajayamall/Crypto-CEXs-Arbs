from common_wss import wss_client
import pandas as pd



class KrakenWSS():

    def __init__(self):
        self.global_dict={}
        self.kraken_order_book_cols = ['price', 'volume', 'timestamp']
        self.stream_url = 'wss://ws.kraken.com'
        self.curreny_pair_arr = [
            "XBT/USD"            ]
        
        
    def order_book_handler(self, response):
        #declaring the trade pair key
        pair_tuple_key = ''
        if(type(response)==type([])):
            pair_tuple_key = (response[0], response[len(response)-1])

        # if array then read the data (only when it is the initial snapshot)
        if(type(response)==type([]) and 'as' in response[1].keys() and 'bs' in response[1].keys()):
            # generating the tuple keys for dict storing all trading pair dataframes
            if(pair_tuple_key not in self.global_dict.keys()):

                # initiating separate df for bid and ask and adding data
                pair_ask = pd.DataFrame(response[1]['as'], columns=self.kraken_order_book_cols)
                pair_bid = pd.DataFrame(response[1]['bs'], columns=self.kraken_order_book_cols)

                #adding key for the trade pair to the global_dict
                self.global_dict[pair_tuple_key] = [pair_ask, pair_bid] # [ask, bid]

        # only when this is update response to the order book and does not contains more than one update 
        elif(type(response)==type([]) and ('a' in response[1].keys() or 'b' in response[1].keys()) and len(response)>=4):

            # looping through the response 
            for val in response:

                #checking if the value in array is object, then does it contain 'a'
                if(type(val) == type({})):
                    currentKey = list(val.keys())[0]
                    dataFrameIndex = 0 if currentKey == 'a' else 1
                    if(len(val.keys())!=1):
                        print('Received more than one key in smame dictionary for update')
                        break
                    for record in val[currentKey]:

                        # condition for deleting existing record, if received value is zero
                        if(record[1]=="0.00000000"):
                            # print('1')
                            '''
                            Remember whenever 0 is encountered following things should happen
                                1. Find the index of the price in the df
                                2. Drop that indexed row from the df
                            '''
                            self.global_dict[pair_tuple_key][dataFrameIndex] = self.global_dict[pair_tuple_key][dataFrameIndex].drop(self.global_dict[pair_tuple_key][dataFrameIndex][self.global_dict[pair_tuple_key][dataFrameIndex].price==record[0]].index)
                            self.global_dict[pair_tuple_key][dataFrameIndex] = self.global_dict[pair_tuple_key][dataFrameIndex].reset_index(drop=True)

                        # condition when updating the current record
                        elif(len(self.global_dict[pair_tuple_key][dataFrameIndex][self.global_dict[pair_tuple_key][dataFrameIndex].price==record[0]].index)>0 and record[1]!="0.00000000"):
                            # print('2')
                            '''
                            Whenever there is update in volume for the price
                                1. Find the row of the record
                                2. Update the volume
                            '''

                            # finding the index of the price equivalent row
                            index = self.global_dict[pair_tuple_key][dataFrameIndex][self.global_dict[pair_tuple_key][dataFrameIndex].price==record[0]].index[0]
                            # updating the volume
                            self.global_dict[pair_tuple_key][dataFrameIndex].iloc[index,].price = record[0]
                            self.global_dict[pair_tuple_key][dataFrameIndex].iloc[index,].volume = record[1]

                        elif(len(self.global_dict[pair_tuple_key][dataFrameIndex][self.global_dict[pair_tuple_key][dataFrameIndex].price==record[0]].index)==0):
                            # print('3')
                            '''
                            Whenever there is a new record to be added
                                1. just append it as a new row to the existing dataframe
                            '''
                            self.global_dict[pair_tuple_key][dataFrameIndex] = self.global_dict[pair_tuple_key][dataFrameIndex].append(pd.DataFrame([record[0:3]], columns=self.kraken_order_book_cols))

        # only when the update response contains more than one update
        elif(type(response)==type([])):  
            print('Exception recorded')        

    def generate_order_book(self):
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "event": "subscribe",
            "pair": self.curreny_pair_arr,
            "subscription": {
            "name": "book",
            "depth":1000
            }
        }
        my_client.subscribe_public(payload, callback=self.order_book_handler,id_="_krakenSuscribeBook")
        my_client.start()

    def ticker_handler(self, response):
        print('ww')
        print(response)

    def get_price_quote(self):
        print('ww')
        my_client = wss_client.WssClient(self.stream_url)
        payload = {
            "event": "subscribe",
            "pair": self.curreny_pair_arr,
            "subscription": {
            "name": "ticker",
            }
        }
        my_client.subscribe_public(data=payload, callback=self.ticker_handler,id_="_krakenSuscribeTicker")
        my_client.start()



    

krakenWss = KrakenWSS()
krakenWss.get_price_quote()