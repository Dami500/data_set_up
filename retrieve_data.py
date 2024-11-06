from __future__ import print_function
import pandas as pd
import mysql.connector as msc



if __name__ == "__main__":
    # Connect to the MySQL instance
    db_host = 'localhost'
    db_user = 'sec_user'
    db_pass = 'Damilare20$'
    db_name = 'securities_master'
    con = msc.connect(host=db_host, user=db_user, passwd=db_pass, db=db_name, connect_timeout=28800)
    # Select all the historic Google adjusted close data
    sql = """SELECT dp.‘price_date‘, dp.‘close_price‘
    FROM securities_master.‘daily_price‘ AS dp
    INNER JOIN securities_master.‘symbol‘ AS sym
    ON dp.‘symbol_id‘ = sym.‘id‘
    ORDER BY dp.‘price_date‘ ASC;
    """
    # Create a pandas dataframe from the SQL query
    goog = pd.read_sql(sql, con= con)
    print(goog.tail())
