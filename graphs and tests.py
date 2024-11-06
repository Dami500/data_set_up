import pandas
import matplotlib.pyplot as plt
import mysql.connector as msc
import datetime
import scipy.stats as stats
from time_series_tests import obtain_data_from_sec_master

db_host = 'localhost'
db_user = 'sec_user'
db_pass = 'Damilare20$'
db_name = 'securities_master'
plug ='caching_sha2_password'
con = msc.connect(host=db_host, user=db_user, password=db_pass, db=db_name, auth_plugin= plug)

start_date = datetime.datetime(2024,8, 1)
end_date = datetime.datetime(2024, 10, 31)
security = 'GOOG'
