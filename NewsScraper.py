import requests
from bs4 import BeautifulSoup

class NewsScraper():
    def __init__(self):
        pass

    def get_articles(self, ticker):
        '''
        Returns a list of tuples with the title, date, and link to articles about the given company
        '''
        articles = []
        URL = 'https://www.nasdaq.com/market-activity/stocks/' + ticker.lower() + '/news-headlines'
        
        soup = self.get_html(URL)
        results = soup.find_all('li', class_='quote-news-headlines__item')
        for article in results:
            title = article.find('p', class_='quote-news-headlines__item-title')
            date = article.find('span', class_='quote-news-headlines__date')
            link = article.find('a', class_='quote-news-headlines__link')
            article_data = (title.text, date.text, link['href'])
            articles.append(article_data)
        
        return articles

    def get_html(self, URL):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup