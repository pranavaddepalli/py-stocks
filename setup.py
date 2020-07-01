from distutils.core import setup
setup(
    name='py-stocks',
    packages=['py-stocks'],
    version='0.3',
    license='MIT',
    description="py-stocks is a package for retrieving real-time stock data, historical stock data, and stock technical indicators.",
    author='Pranav Addepalli', 
    author_email='pranav.addepalli@gmail.com',
    url='https://github.com/pranavaddepalli/PyStocks',
    download_url='https://github.com/pranavaddepalli/PyStocks/archive/0.2.tar.gz',
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
