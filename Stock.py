import stockquotes as sq
import yfinance as yf
from NewsScraper import NewsScraper

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
        return self.newsScraper.get_articles(self.ticker)

    def get_last_month_data(self):
        return self.sqobj.historical
    
    def get_last_month_open(self):
        return [ (x['date'], x['open']) for x in self.get_last_month_data()]

    def get_last_month_close(self):
        return [ (x['date'], x['close']) for x in self.get_last_month_data()]
    
    def get_last_month_high(self):
        return [ (x['date'], x['high']) for x in self.get_last_month_data()]

    def get_last_month_low(self):
        return [ (x['date'], x['low']) for x in self.get_last_month_data()]
    
    def get_last_month_volume(self):
        return [ (x['date'], x['volume']) for x in self.get_last_month_data()]

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