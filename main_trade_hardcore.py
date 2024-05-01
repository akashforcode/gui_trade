################LOGIC PART##########################################
from tkinter import*

currentsum=0
from tkinter import *
from tkinter import messagebox
from kite_trade import *
from tkinter import*
from kite_trade import *

#################VARIABLE DEFINE#############
call_strike="aa"
put_strike="bb"

lb=[47100, 47200, 47300, 47400, 47500]

cspb=int(input("input strike price for current banknifty:::"))
lb=[cspb-200,cspb-100,cspb,cspb+100,cspb+200]

# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

def start_kite_enc():
    f = open("token.txt", "r")
    enctoken=f.read()
    kite = KiteApp(enctoken=enctoken)
    print(kite.margins())


f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:BANKNIFTY24MAR46000PE"))
##########BANKNIFTY24MAR46600PE


import tkinter as tk
from tkinter import ttk
from datetime import datetime




def refresh():
    print("Refresh Button Clicked")

def show_date():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    date_label.config(text="Current Date: " + current_time)

def on_select(event):
    global call_strike,put_strike
    selected_item1 = dropdown1.get()
    selected_item2 = dropdown2.get()
    call_strike=selected_item1
    put_strike=selected_item2
    print("Selected item 1:", selected_item1,call_strike)
    print("Selected item 2:", selected_item2,put_strike,type(put_strike))


import time
def buy_option(n):
    for i in range(1):
        print(call_strike)
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=call_strike,
                              #tradingsymbol="BANKNIFTY2430646600CE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              #quantity=e1.get(),
                              quantity=n,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=600.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option(n):
    for i in range(1):
        print(call_strike)
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=call_strike,
                              #tradingsymbol="BANKNIFTY2430646600CE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              #quantity=e1.get(),
                              quantity=n,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=600.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def buy_option_put(n):
    for i in range(1):
        print(put_strike)
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=put_strike,
                              #tradingsymbol="BANKNIFTY2430646600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              #quantity=e1.get(),
                              quantity=n,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=600.00,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option_put(n):
    for i in range(1):
        print(put_strike)
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=put_strike,
                              #tradingsymbol="BANKNIFTY2430646600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              #quantity=e1.get(),
                              quantity=n,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=600.00,
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

#lb=[47100, 47200, 47300, 47400, 47500]

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


##############LOGIC PART##############################################




    
# Create main window
root = tk.Tk()
root.title("BankNifty")

# Big input box with title
big_input_label = tk.Label(root, text="TOKEN")
big_input_label.grid(row=0, column=0, sticky="w")
big_input = tk.Text(root, height=2, width=70)
big_input.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Combo boxes

############COMBO BOX###################
# Create first dropdown menu
options1 = lbsc
dropdown1 = ttk.Combobox(root, values=options1)
dropdown1.current(0)  # Set default selection
dropdown1.bind("<<ComboboxSelected>>", on_select)
dropdown1.grid(row=1, column=1, padx=5, pady=5)

# Create second dropdown menu
options2 =lbsp
dropdown2 = ttk.Combobox(root, values=options2)
dropdown2.current(0)  # Set default selection
dropdown2.bind("<<ComboboxSelected>>", on_select)
dropdown2.grid(row=1, column=3, padx=5, pady=5)
############COMBO BOX###################


# Buttons
def button_command(button_num):
    print("Button {} Clicked".format(button_num))
    #buy_option()



button2 = tk.Button(root, text="15", command=lambda: buy_option(15))
button2.grid(row=5, column=0, padx=5, pady=5)

button3 = tk.Button(root, text="30", command=lambda: buy_option(30))
button3.grid(row=6, column=0, padx=5, pady=5)

button4 = tk.Button(root, text="60", command=lambda: buy_option(60))
button4.grid(row=7, column=0, padx=5, pady=5)

button5 = tk.Button(root, text="90", command=lambda: buy_option(90))
button5.grid(row=8, column=0, padx=5, pady=5)



button7 = tk.Button(root, text="15", command=lambda: sell_option(15))
button7.grid(row=5, column=1, padx=5, pady=5)

button8 = tk.Button(root, text="30", command=lambda: sell_option(30))
button8.grid(row=6, column=1, padx=5, pady=5)

button9 = tk.Button(root, text="60", command=lambda: sell_option(60))
button9.grid(row=7, column=1, padx=5, pady=5)

button10 = tk.Button(root, text="90", command=lambda: sell_option(90))
button10.grid(row=8, column=1, padx=5, pady=5)



button12 = tk.Button(root, text="15", command=lambda: buy_option_put(15))
button12.grid(row=5, column=2, padx=5, pady=5)

button13 = tk.Button(root, text="30", command=lambda: buy_option_put(30))
button13.grid(row=6, column=2, padx=5, pady=5)

button14 = tk.Button(root, text="60", command=lambda: buy_option_put(60))
button14.grid(row=7, column=2, padx=5, pady=5)

button15 = tk.Button(root, text="90", command=lambda: buy_option_put(90))
button15.grid(row=8, column=2, padx=5, pady=5)



button17 = tk.Button(root, text="15", command=lambda: sell_option_put(15))
button17.grid(row=5, column=3, padx=5, pady=5)

button18 = tk.Button(root, text="30", command=lambda: sell_option_put(30))
button18.grid(row=6, column=3, padx=5, pady=5)

button19 = tk.Button(root, text="60", command=lambda: sell_option_put(60))
button19.grid(row=7, column=3, padx=5, pady=5)

button20 = tk.Button(root, text="90", command=lambda: sell_option_put(90))
button20.grid(row=8, column=3, padx=5, pady=5)

# Refresh Button
refresh_button = tk.Button(root, text="Refresh", command=refresh)
refresh_button.grid(row=9, column=1, sticky="ew", padx=15, pady=0)

# START Button
refresh_button = tk.Button(root, text="START", command=start_kite_enc)
refresh_button.grid(row=12, column=1, sticky="ew", padx=15, pady=0)

# Date Button
date_button = tk.Button(root, text="Show Date", command=show_date)
date_button.grid(row=10, column=1, sticky="ew")

# Date Label
date_label = tk.Label(root, text="")
date_label.grid(row=11, column=1, columnspan=2, padx=10, pady=5)


root.mainloop()