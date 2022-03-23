# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:00:10 2022

@author: Topher
"""
from yahoo_fin import stock_info as si
import yfinance as yf
import random

riskrating = input('On a scale from 1 to 3, how lucky do you feel? ')
if riskrating == '1':
    stonks = si.tickers_dow()
    print("super duper lame")
    
elif riskrating == '2':
    stonks = si.tickers_sp500()
    print("lame")
    
else:
    print("That's what I like to see")
    stonks = si.tickers_nasdaq()
        

luckychoiceticker = stonks[random.randint(0,len(stonks))]
luckychoiceinfo = yf.Ticker(luckychoiceticker)
luckychoicedescription = luckychoiceinfo.info
print(luckychoicedescription['longName'])
print(luckychoiceticker)
print(luckychoicedescription['longBusinessSummary'])