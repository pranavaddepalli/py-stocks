import stockquotes as sq
import yfinance as yf
import requests
from bs4 import BeautifulSoup

def scrape_news_text(news_url):
    print('scraping news text')
    news_html = requests.get(news_url).content
 
    '''convert html to BeautifulSoup object'''
    news_soup = BeautifulSoup(news_html , 'lxml')
 
    paragraphs = [par.text for par in news_soup.find_all('p')]
    news_text = '\n'.join(paragraphs)
 
    return news_text

def get_news_urls(links_site):
    print('getting news urls')
    '''scrape the html of the site'''
    resp = requests.get(links_site)
    print('got response')
    if not resp.ok:
        return None
 
    html = resp.content
 
    '''convert html to BeautifulSoup object'''
    soup = BeautifulSoup(html , 'lxml')
 
    '''get list of all links on webpage'''
    print('getting all links with a')
    links = soup.find_all('a')
    print(links)
    urls = [link.get('href') for link in links]
    urls = [url for url in urls if url is not None]
 
    '''Filter the list of urls to just the news articles'''
    news_urls = [url for url in urls if '/article/' in url]
 
    return news_urls

class Stock:
    def __init__(self, symbol):
        self.ticker = symbol.upper()
        
        self.sqobj = sq.Stock(self.ticker)
        self.yfobj = yf.Ticker(self.ticker)
        self.info = self.yfobj.get_info()

    def get_ticker(self):
        return self.ticker

    def get_news(self, upper_page_limit = 1):
        print('getting news')
        landing_site = 'https://www.nasdaq.com/market-activity/stocks/' + self.ticker.lower() + '/news-headlines'
        print('landing site: ', landing_site)
        all_news_urls = get_news_urls(landing_site)
        print('got all urls')
        current_urls_list = all_news_urls.copy()
        index = 2
        print(index)
        while (current_urls_list is not None) and (current_urls_list != []) and (index <= upper_page_limit):
            current_site = landing_site + '?page=' + str(index)
            current_urls_list = get_news_urls(current_site)
            all_news_urls = all_news_urls + current_urls_list
            print(index)
            index = index + 1
            
        all_news_urls = list(set(all_news_urls))
        all_articles = [scrape_news_text(news_url) for news_url in all_news_urls]
        return all_articles

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