import yfinance as yf
from symbols import obtain_parse_wiki_snp500
import pandas as pd
import mysql.connector as msc
import warnings
import numpy as np
warnings.filterwarnings('ignore')

db_host = 'localhost'
db_user = 'sec_user'
db_pass = 'Damilare20$'
db_name = 'securities_master'
plug ='caching_sha2_password'
con = msc.connect(host=db_host, user=db_user, password=db_pass, db=db_name, auth_plugin= plug)

# aapl = yf.Ticker('AAPL')
# print(aapl.info.get('marketCap'))
# print(aapl.financials)
# print(aapl.quarterly_balance_sheet.T)
# print(aapl.major_holders)
# data2 = aapl.balance_sheet.loc[['Total Debt', 'Stockholders Equity', 'Current Assets', 'Current Liabilities', 'Tangible Book Value']]
# print(data2.T.reset_index())
#
#
# data = aapl.financials.loc[['Basic EPS','Diluted EPS','Net Income', 'EBIT', 'EBITDA', 'Gross Profit', 'Operating Revenue', 'Total Revenue']]
# print(data.T.reset_index())
# # # data = data.T
# # # print(data)
# #
# tickers = [i[0] for i in obtain_parse_wiki_snp500()]
# print(tickers[1:503])

def get_fundamentals_dataframe(tick, symbol_id):
    """Obtains all the fundamental data we care about into a single dataframe
    for iteration into our database
    """
    ticker_object = yf.Ticker(tick)
    df1 = ticker_object.financials.loc[['Basic EPS','Diluted EPS','Net Income', 'EBIT', 'EBITDA', 'Gross Profit', 'Operating Revenue', 'Total Revenue']]
    df1 = df1.T.reset_index()
    df2 = ticker_object.balance_sheet.loc[['Total Debt', 'Stockholders Equity', 'Current Assets', 'Current Liabilities', 'Tangible Book Value']]
    df2 = df2.T.reset_index()
    final_df = pd.merge(df1, df2, how = 'inner', on = df1['index'])
    final_df.drop(columns = ['index_y', 'key_0'], inplace = True)
    final_df['symbol_id'] = [symbol_id for i in range(0, len(final_df))]
    final_df['market_cap'] = [ticker_object.info.get('marketCap') for i in range(0, len(final_df))]
    return final_df


def insert_financials_into_sql_database(data):
    """This function collects fundamental data using the yfinance API
    Data for every ticker symbol in securities master is taken
    """
    records = []
    for i in range(len(data.index)):
        tup = (data.iloc[i,0],data.iloc[i,1], data.iloc[i,2], data.iloc[i,3], data.iloc[i,4], data.iloc[i,5],
               data.iloc[i,6], data.iloc[i,7], data.iloc[i,8], data.iloc[i,9], data.iloc[i,10], data.iloc[i,11],
               data.iloc[i,12], data.iloc[i,13], data.iloc[i,14], data.iloc[i,15])
        records.append(tup)
    insert_str = """insert into securities_master.fundamentals (securities_master.fundamentals.symbol_id, securities_master.fundamentals.date,
    securities_master.fundamentals.basic_EPS, securities_master.fundamentals.diluted_EPS, securities_master.fundamentals.net_income,
    securities_master.fundamentals.ebit, securities_master.fundamentals.ebitda, securities_master.fundamentals.gross_profit,
    securities_master.fundamentals.operating_revenue, securities_master.fundamentals.total_revenue, securities_master.fundamentals.total_debt,
    securities_master.fundamentals.stockholder_equity, securities_master.fundamentals.current_assets, securities_master.fundamentals.current_liablilities,
    securities_master.fundamentals.tangible_book_value) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
    cur = con.cursor()
    cur.executemany(insert_str, records)


# data = get_fundamentals_dataframe('AAPL', 1)
# print(data)
# data_2 = insert_financials_into_sql_database(data)
# print(data_2)

if __name__ == '__main__':
    tickers = [i[0] for i in obtain_parse_wiki_snp500()]
    tickers = tickers[1:503]
    i = 1











