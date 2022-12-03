
from config import api_key, api_secret
from binance.client import Client
import time
from tradingview_ta import TA_Handler, Interval, Exchange

Symbol = 'BTCUSDT'
Interval_1 = Interval.INTERVAL_1_DAY
Interval_2 = Interval.INTERVAL_4_HOURS
Qnty = 50

client = Client(api_key, api_secret)

def get_data():
    output_1 = TA_Handler(symbol=Symbol, screener='Crypto', exchange='Binance', interval=Interval_1)
    output_2 = TA_Handler(symbol=Symbol, screener='Crypto', exchange='Binance', interval=Interval_2)

    activiti_1 = output_1.get_analysis().summary
    activiti_2 = output_2.get_analysis().summary
    return 'D1', activiti_1, 'H4', activiti_2

def main():
    buy = False
    sell = True
    print('Script running...')
    while True:
        data = get_data()
        print(Symbol, data)
        time.sleep(19)

if __name__ == '__main__':
    main()


