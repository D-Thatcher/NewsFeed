import pandas as pd
import numpy as np


def get_frame(file, sheet_name):
    return pd.read_excel(file, sheet_name=sheet_name)

def settings_clean(ls):
    return [i.strip().lower() for i in ls if i is not np.nan]

def get_settings():
    df = get_frame(r"C:\Users\DanLa\PycharmProjects\NewsFeed\DataCompany.xlsx", sheet_name='Settings')
    remove = settings_clean(list(df['Remove']))
    highlight = settings_clean(list(df['Preset Highlight']))
    return remove, highlight

def clean(ls):
    store = []
    for i in ls:
        if i is not np.nan:
            store.append(i.replace(',','').replace('.',''))
    return store

def ticker_clean(ls):
    return [i for i in ls if i is not np.nan]

def reduce_pair(pair):
    if len(pair)==1:
        return pair[0]
    else:
        return pair[0]+" "+pair[1]

def ticker_map_et_all():
    df = get_frame(r"C:\Users\DanLa\PycharmProjects\NewsFeed\DataCompany.xlsx", sheet_name='Companies')

    interest = ["Symbol1","Name1",	"Symbol2",	"Name2"	,"Symbol3",	'Name3'	,'Ticker4'	,'Name4',	'Ticker5',	'Name5'	]

    s1 = ticker_clean(list(df['Symbol1']))
    n1 = clean(list(df['Name1']))
    assert(len(s1)==len(n1)and len(s1)>0)

    s2 = ticker_clean(list(df['Symbol2']))
    n2 = clean(list(df['Name2']))
    assert(len(s2)==len(n2)and len(s2)>0)

    s3 = ticker_clean(list(df['Symbol3']))
    n3 = clean(list(df['Name3']))
    assert(len(s3)==len(n3)and len(s3)>0)

    s4 = ticker_clean(list(df['Ticker4']))
    n4 = clean(list(df['Name4']))
    assert(len(s4)==len(n4)and len(s4)>0)

    s5 = ticker_clean(list(df['Ticker5']))
    n5 = clean(list(df['Name5']))
    assert(len(s5)==len(n5)and len(s5)>0)

    t1 = {n1[i]:s1[i] for i in range(0,len(s1))}
    t2 = {n2[i]:s2[i] for i in range(0,len(s2))}
    t3 = {n3[i]:s3[i] for i in range(0,len(s3))}
    t4 = {n4[i]:s4[i] for i in range(0,len(s4))}
    t5 = {n5[i]:s5[i] for i in range(0,len(s5))}

    all_ticker = {}
    all_ticker.update(t1)
    all_ticker.update(t2)
    all_ticker.update(t3)
    all_ticker.update(t4)
    all_ticker.update(t5)

    p = ['OneP',	'TwoP'	,'ThreeP',	'FourP'	,'FiveP',	'SixP']
    all_non_exchange = []

    for i in range(0,len(p)):
        all_non_exchange+=(clean(list(df[p[i]]))[1:])

    for i in range(0,5):
        all_non_exchange+=(clean(list(df["Name"+str(i+1)])))

    all_non_exchange = list(set(all_non_exchange))

    first_for_search = []
    two_for_search = []

    for i in all_non_exchange:
        s =i.split(' ')
        f = s[0].strip().lower()
        first_for_search.append(f)
        if len(s)>1:
             two_for_search.append(f + " " + s[1].strip().lower())
        else:
             two_for_search.append(f)


    idx_hash = {i:[] for i in two_for_search}
    for i in range(0,len(all_non_exchange)):
        curr = idx_hash[two_for_search[i]]
        curr.append(i)
        idx_hash[two_for_search[i]] = curr


    return all_ticker, first_for_search, idx_hash, all_non_exchange, two_for_search








