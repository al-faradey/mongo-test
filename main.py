# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
from pydataset import data
import datetime
from datetime import timedelta
import random
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    td_series = pd.Series()
    td_series = [random.random() * datetime.timedelta(hours=1) for i in range(10000)]


    # generate start & end datetime
    def random_dates(start, end, n=10000):
        start_u = start.value // 10 ** 9
        end_u = end.value // 10 ** 9
        return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')


    start = pd.to_datetime('2015-01-01')
    end = pd.to_datetime('2018-01-01')
    start_date = random_dates(start, end)
    pd_start_date = pd.DataFrame(start_date)

    pd_end_date = pd_start_date.copy()

    print(pd_end_date.head(5))
    random.seed(20)
    for i in range(len(pd_end_date)):
        pd_end_date.iloc[i] = pd_end_date[i] + timedelta(minutes=random.randint(1, 10))

    # generate urls
    dat = data()
    dict_words = []
    whole_string = ''
    for i in range(len(dat['title'])):
        whole_string += (dat['title'][i])
    words_dict = whole_string.split()
    domain_list = ['.ru', '.com', '.org', '.gov', '.rf', '.kz', '.us', '.cz']

    urls = pd.Series()
    ips = pd.Series()

    for i in range(10000):
        rand_name = random.randint(0, len(words_dict) - 1)
        rand_domain = random.randint(0, len(domain_list) - 1)
        url = 'www.' + words_dict[rand_name] + domain_list[rand_domain]
        urls[len(urls)] = url
        ips[len(ips)] = str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(
            random.randint(1, 255)) + '.' + str(random.randint(1, 255))

    db_ext = pd.concat([urls, ips, pd_start_date, pd_end_date], axis=1)
    db_ext.columns = ['url', 'usr_ip', 'start_datetime', 'end_datetime']
    db_ext['visit_length'] = pd.to_datetime(db_ext['end_datetime']) - pd.to_datetime(db_ext['start_datetime'])
