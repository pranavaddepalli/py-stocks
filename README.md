# PyStocks
PyStocks is a package for retrieving real-time stock data, historical stock data, and stock technical indicators.

# Usage
Create a new `Stock` object with the ticker symbol:
```python

microsoft = Stock("MSFT")
```

## Basic Company Data
```python
# get full company name
microsoft.get_name()

# get company sector
microsoft.get_sector()

# get company industry
microsoft.get_industry()

# get number of employees
microsoft.get_employees()

# get company address
microsoft.get_address()

# get company website
microsoft.get_website()

# get company institutional holders as a pandas DataFrame object
microsoft.get_holders()

# get company sustainability information as a pandas DataFrame object
microsoft.get_sustainability_info()

# get all analyst recommendations as a pandas DataFrame object
microsoft.get_analyst_recs()

# get most recent analyst recommendations as a pandas DataFrame object
microsoft.get_most_recent_recs()

# get company summary
microsoft.get_summary()
```

## Technical Data
```python
# get recent news articles from NASDAQ as a pandas DataFrame object
microsoft.get_news()

# get current stock price
microsoft.get_current_price()

# get stock volume
microsoft.get_volume()

# get stock average volume
microsoft.get_average_volume()

# get stock dividend yield
microsoft.get_dividend_yield()

# get stock day high
microsoft.get_day_high()

# get stock day low
microsoft.get_day_low()

# get stock 52 week high
microsoft.get_52week_high()

# get stock 52 week low
microsoft.get_52week_low()

# get stock EMA for the previous month as a pandas DataFrame object
microsoft.get_month_ema()

# get stock open, close, high, low, and volume data for the previous month as a pandas DataFrame object
microsoft.get_last_month_data()

# get stock open data for the previous month as a pandas DataFrame object
microsoft.get_last_month_open()

# get stock close data for the previous month as a pandas DataFrame object
microsoft.get_last_month_close()

# get stock high data for the previous month as a pandas DataFrame object
microsoft.get_last_month_high()

# get stock low data for the previous month as a pandas DataFrame object
microsoft.get_last_month_low()

# get stock volume data for the previous month as a pandas DataFrame object
microsoft.get_last_month_volume()

```
# Requirements
1. pandas
2. datetime
3. requests
4. BeautifulSoup4
5. stockquotes
6. yfinance
