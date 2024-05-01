import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
from tkinter import*

currentsum=0
from tkinter import *
from tkinter import messagebox
from kite_trade import *
import pandas as pd



# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:TRIDENT"))

#####DATE 
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
########################DATE################
def background_task():
    # Simulating a time-consuming task
    i=0
    while True:
        i=i+1
        time.sleep(1)
        print("Background Task:", i)
        #print(kite.ltp("NSE:NIFTY BANK"))
        nb=pd.DataFrame(kite.ltp("NSE:NIFTY BANK"))
        intnb=int(nb.iat[1, 0])
        print(intnb)
        print((round(intnb/100))*100)
        bs=((round(intnb/100))*100)
        bsl=[bs-200,bs-100,bs,bs+100,bs+100]
        print(bsl)


def start_background_task():
    thread = Thread(target=background_task)
    thread.start()

# Create a Tkinter window
window = tk.Tk()
window.title("Multithreading Example")

# Create a button to start the background task
start_button = ttk.Button(window, text="Start Background Task", command=start_background_task)
start_button.pack(pady=20)

window.mainloop()