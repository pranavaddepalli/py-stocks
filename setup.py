from distutils.core import setup
setup(
    name='PyStocks',
    packages=['PyStocks'],
    version='0.1',
    license='MIT',
    description='PyStocks is a package for retrieving real-time stock data, historical stock data, and stock technical indicators.',
    author='Pranav Addepalli', 
    author_email='pranav.addepalli@gmail.com',
    url='https://github.com/pranavaddepalli/PyStocks',
    download_url='https://github.com/pranavaddepalli/PyStocks/archive/v_0.1.tar.gz',
    keywords=['Finance', 'Stocks', 'Python', 'Scraper'],
    install_requires=[
        'stockquotes',
        'yfinance',
        'pandas',
        'beautifulsoup4',
        'datetime',
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
