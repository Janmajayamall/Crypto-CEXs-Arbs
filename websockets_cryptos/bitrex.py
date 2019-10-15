# from bittrex_websocket.websocket_client import BittrexSocket
# from time import sleep

# tickers = {
#     'ZCL':  (35, 5),
#     'RDD': (20000, 2000),
#     'TRX': (5000, 2000),
# }


# class BittrexSocket1(BittrexSocket):
#         def __init__(self, tickers, url=None):
#             super(BittrexSocket1, self).__init__(url)
#             self.tickers = tickers
#             self.cnt = 0
#             for ticker in self.tickers:
#                 sleep(0.01)
#                 self.query_exchange_state(['BTC-'+ticker])


#         def on_public(self, msg):
#             print(msg)
#             ticker = msg['M'].split('-')[-1]
#             self.cnt += 1
#             return

# def main():
#     ws = BittrexSocket1(tickers)
#     ws.enable_log()
#     try:
#         while True:
#             sleep(60)
#     except KeyboardInterrupt:
#         pass
#     ws.disconnect()
#     sleep(10)

# if __name__ == "__main__":
#     main()