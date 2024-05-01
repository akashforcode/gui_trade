from tkinter import*

currentsum=0
from tkinter import *
from tkinter import messagebox
from kite_trade import *




# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:BANKNIFTY24MAR46000PE"))
##########BANKNIFTY24MAR46600PE

import time
def buy_option():
    for i in range(1):
        print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=e2.get(),
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=e1.get(),
                              #quantity=15*e1.get(),
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option():
    for i in range(1):
        print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=e2.get(),
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=e1.get(),
                              #quantity=15*e1.get(),
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)
import pandas as pd


import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

def next_wednesday():
    today = datetime.today()
    days_ahead = (2 - today.weekday()) % 7  # Calculate days until next Wednesday (Wednesday is represented by 2)
    next_wednesday_date = today + timedelta(days=days_ahead)
    return next_wednesday_date.strftime("%Y-%m-%d")

print("Date of upcoming Wednesday:", next_wednesday())



yr=int(next_wednesday()[2:4])
mm=int(next_wednesday()[5:7])
dd=(next_wednesday()[8:10])
print(yr,mm,dd)

yr=str(yr)
mm=str(mm)
dd=str(dd)

datew=yr+mm+dd
bankoptionputpe="BANKNIFTY"+datew+"46800"+"PE"
print(bankoptionputpe)

lb=[47100, 47200, 47300, 47400, 47500]

lbsp=[]
lbsc=[]
for i in range(5):
    bankoptionputpe="BANKNIFTY"+datew+str(lb[i])+"PE"
    bankoptionputce="BANKNIFTY"+datew+str(lb[i])+"CE"
    lbsp.append(bankoptionputpe)
    lbsc.append(bankoptionputce)
print(bankoptionputpe)
print(bankoptionputce)

print(lbsp)
print(lbsc)


while True:
    #print(kite.ltp("NFO:BANKNIFTY24MAR46000PE"))
    new1 = pd.DataFrame.from_dict((kite.ltp("NSE:NIFTY BANK")))#print(new1)
    print(new1.iat[1, 0])
    nbr=int((round((new1.iat[1, 0])/100))*100)
    print(nbr)
    nbrsl=[nbr-200,nbr-100,nbr,nbr+100,nbr+200]
    print(nbrsl)
    time.sleep(1)