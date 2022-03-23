# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:00:10 2022

@author: Topher
"""
from yahoo_fin import stock_info as si
import yfinance as yf
import random

tickers = si.tickers_sp500()
luckychoiceticker = tickers[random.randint(0,len(tickers))]
luckychoiceinfo = yf.Ticker(luckychoiceticker)
luckychoicedescription = luckychoiceinfo.info
print(luckychoicedescription['longName'])
print(luckychoiceticker)
print(luckychoicedescription['longBusinessSummary'])

