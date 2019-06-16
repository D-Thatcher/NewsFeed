import feedparser
from functools import reduce
import time
from datetime import datetime



def burn_feed_burner(summary):
    return summary.split('<')[0]

def get_preset():
    h = []
    with open(r"C:\Users\DanLa\PycharmProjects\NewsFeed\presethighlight.txt",'r') as f:
        for line in f:
            line = line.strip().lower()
            if len(line)>0:
                h.append(line)
    return h

def ERR_url_from_preset(h):
    return ["https://news.google.com/rss/search?q=" + i for i in h]


def word_sum(x1, x2): return x1 + " "+ x2


def filter_title(title):
    title = title.replace('&apos;', '').strip()
    s = title.split(':')
    if len(s)>1:
        if len(s[0]) < 23:
            return reduce(word_sum,s[1:]).strip()
    return title.strip()



def coerce_date(item,item_feed):
    if ('published_parsed' not in item_feed) or item['published_parsed'] is None:
        if 'published' in item_feed:
            # Expect format' Apr 18, 2019 05:59 GMT' and form struct accordingly
            try:
                # Assume format of published: 'Apr 18, 2019 05:59 GMT'
                item_feed['published_parsed'] = datetime.strptime(item_feed['published'],
                                                                  '%b %d, %Y %H:%M %Z').timetuple()

            except Exception as e:
                item_feed['published_parsed'] = time.struct_time((2019, 4, 19, 0, 56, 14, 4, 109, 0))
        else:
            # Give pub parsed an arbitrary struct so sorting and further uses do not go wonky.
            item_feed['published'] = 'Apr 18, 2019 05:59 GMT'
            item_feed['published_parsed'] = time.struct_time((2019, 4, 19, 0, 56, 14, 4, 109, 0))
    return item_feed


def get_feed(lo_url):

    item_feed = {}
    interest = ['title','link','summary','published','published_parsed']
    lo_item = []

    for url in lo_url:
        items = feedparser.parse( url )['items']
        for item in items:

            for item_of_interest in interest:
                if item_of_interest in item:

                    if item_of_interest == 'title':
                        item_feed['reddit'] = False
                        item_feed['twitter'] = False
                        item_feed[item_of_interest] = filter_title(item[item_of_interest])
                    elif item_of_interest == 'summary':
                            item_feed[item_of_interest] = burn_feed_burner(item[item_of_interest])
                    else:
                        item_feed[item_of_interest] = item[item_of_interest]

                    # if item_of_interest == 'title':
                    #     if 'bankruptcy code' in item_feed[item_of_interest].lower():
                    #         print(url)
                    #         print(item_feed[item_of_interest])
                    #         print(item[item_of_interest])

            item_feed = coerce_date(item,item_feed)

            lo_item.append(item_feed)
            item_feed = {}

    return lo_item
#
# def date_portion(date):
#     splt = date.split(' ')[:3]
#     if len(splt)<3:
#         print(date)
#     return splt[0] + " " + splt[1] + " " +  splt[2]
#
# import Constants
# f= get_feed(Constants.RSS_FEED_GENERAL)
# for i in f:
#     try:
#         date_portion(i['published'])
#     except Exception as e:
#         print(repr(e))
#         print(i)
#         print(i['published'])
# p = '2019-04-19 01:48:36'
preset_highlight = get_preset()
