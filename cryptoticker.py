#! python
import requests
import json
from tkinter import *
import tkinter.font as tkFont
import time

root = Tk()
root.title('Crypto Price Ticker')
fontStyle = tkFont.Font(size=20)

coins = ['dogecoin', 'bitcoin', 'ethereum','litecoin','ravencoin','tron']
prices = {'dogecoin': StringVar()}
prices['dogecoin']


for i in range(0,len(coins)):
    Label(root,text=coins[i],font=fontStyle).grid(row=i,column=0)

    prices[coins[i]] = StringVar()
    prices[coins[i]].set('fetching...')
    
    Entry(root,font=fontStyle,fg='green', textvariable = prices[coins[i]]).grid(row=i, column=1)

def get_price():
    while True:
        for coin in coins:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+coin+'&vs_currencies=inr')
            data = json.loads(response.content)
            prices[coin].set(str(data[coin]['inr'])+'₹')
            #print(data)
            print(coin+str(data[coin]['inr'])+'₹')
            root.update()
        
        time.sleep(10)

root.after(1000, get_price)

root.mainloop()
