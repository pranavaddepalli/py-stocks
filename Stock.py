import stockquotes as sq
import yfinance as yf
import pandas as pd
import numpy as np
from NewsScraper import NewsScraper
import datetime

class Stock:
    def __init__(self, symbol):
        self.ticker = symbol.upper()
        self.newsScraper = NewsScraper()
        self.sqobj = sq.Stock(self.ticker)
        self.yfobj = yf.Ticker(self.ticker)
        self.info = self.yfobj.get_info()

    def get_ticker(self):
        return self.ticker

    def get_news(self):
        news = pd.DataFrame(self.newsScraper.get_articles(self.ticker))
        news.columns=['title', 'date', 'URL']
        return news

    def get_last_month_data(self):
        df = pd.DataFrame(self.sqobj.historical)
        df.set_index('date', inplace=True)
        return df
    
    def get_last_month_open(self):
        df = self.get_last_month_data()['open'].to_frame()
        df.columns=['open']
        return df        

    def get_last_month_close(self):
        df = self.get_last_month_data()['close'].to_frame()
        df.columns=['close']
        return df  
    
    def get_last_month_high(self):
        df = self.get_last_month_data()['high'].to_frame()
        df.columns=['high']
        return df  

    def get_last_month_low(self):
        df = self.get_last_month_data()['high'].to_frame()
        df.columns=['high']
        return df  
    
    def get_last_month_volume(self):
        df = self.get_last_month_data()['volume'].to_frame()
        df.columns=['volume']
        return df  

    def get_current_price(self):
        return self.sqobj.current_price

    def get_name(self):
        return self.info['longName']

    def get_sector(self):
        return self.info['sector']
    
    def get_industry(self):
        return self.info['industry']

    def get_employees(self):
        return self.info['fullTimeEmployees']
    
    def get_summary(self):
        return self.info['longBusinessSummary']
    
    def get_address(self):
        return (self.info['address1'] + ', ' + self.info['city'] + ', ' + self.info['state'] + ', ' + self.info['zip'] + ', ' + self.info['country'])

    def get_website(self):
        return self.info['website']

    def get_average_volume(self):
        return self.info['averageVolume'] 

    def get_volume(self):
        return self.info['volume']

    def get_dividend_yield(self):
        return self.info['dividendYield']

    def get_day_high(self):
        return self.info['dayHigh']
    
    def get_day_low(self):
        return self.info['dayLow']

    def get_52week_high(self):
        return self.info['fiftyTwoWeekHigh']

    def get_52week_low(self):
        return self.info['fiftyTwoWeekLow']
    
    def get_holders(self):
        return self.yfobj.institutional_holders

    def get_sustainability_info(self):
        return self.yfobj.sustainability

    def get_analyst_recs(self):
        return self.yfobj.recommendations
    
    def get_most_recent_recs(self):
        return self.yfobj.recommendations.tail()