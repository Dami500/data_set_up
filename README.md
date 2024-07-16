These are the Python Scripts I use for algorithmic trading.

Symbols.py obtains the tickers for the companies on the S&P 500 as well as their sector and currency and stores it on an SQL database

Price retrieval.py collects pricing data from the Yahoo finance API and stores it on a table in an SQL database. I find it easier to keep all pricing data stored there

I download CSV files containing pricing data for futures contracts from the nasdaqdatalink. futures.py reads this data into a dataframe and visualizes it using seaborn 

Retrieve data.py is a test page that collects data from my SQL database into a dataframe. 

I currently working on sequential learning techniques to develop models for trading using interactive brokers. 
