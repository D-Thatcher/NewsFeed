# Constants
#CNN
RSS_FEED_GENERAL = [
"http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
"http://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
"http://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
"http://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml",
"http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
"https://rss.nytimes.com/services/xml/rss/nyt/Dealbook.xml",
"http://rss.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml",
"https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
"https://feeds.a.dj.com/rss/RSSWSJD.xml",
"https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
"https://finance.yahoo.com/rss/industry?s=yhoo",
"https://feeds.finance.yahoo.com/rss/2.0/headline?s=yhoo",
"https://finance.yahoo.com/rss/topstories",
"https://www.economist.com/business/rss.xml",
"https://www.economist.com/finance-and-economics/rss.xml",
"https://news.google.com/news/rss/headlines/section/topic/BUSINESS",
"http://feeds.marketwatch.com/marketwatch/topstories/",
"http://feeds.marketwatch.com/marketwatch/marketpulse/",
"http://feeds.marketwatch.com/marketwatch/mutualfunds/",
"http://feeds.marketwatch.com/marketwatch/financial/",
"http://feeds.marketwatch.com/marketwatch/StockstoWatch/",
"http://feeds.marketwatch.com/marketwatch/software/",
"http://feeds.reuters.com/reuters/businessNews",
"http://feeds.reuters.com/reuters/companyNews",
"http://feeds.reuters.com/news/wealth",
"https://news.google.com/rss/search?q=leveraged+buyout",
"https://news.google.com/rss/search?q=LBO",
"https://news.google.com/rss/search?q=buyout",
"https://news.google.com/rss/search?q=acquire",
"https://news.google.com/rss/search?q=acquisition",
"https://news.google.com/rss/search?q=merger",
"https://news.google.com/rss/search?q=ipo",
"https://news.google.com/rss/search?q=initial+public+offering",
"http://rss.cnn.com/rss/money_markets.rss",
"http://rss.cnn.com/rss/money_latest.rss",
"http://rss.cnn.com/rss/money_news_companies.rss",
"http://rss.cnn.com/rss/money_technology.rss",
"http://rss.cnn.com/rss/money_topstories.rss",
"https://seekingalpha.com/tag/ipo-analysis.xml",
"https://seekingalpha.com/market_currents.xml",
"https://seekingalpha.com/sector/financial.xml",
"https://ca.investing.com/rss/stock_Fundamental.rss",
"https://ca.investing.com/rss/stock_Technical.rss",
"https://ca.investing.com/rss/stock_Stocks.rss",
"https://ca.investing.com/rss/commodities_Technical.rss",
"https://ca.investing.com/rss/commodities_Fundamental.rss",
"https://ca.investing.com/rss/commodities_Opinion.rss",
"https://ca.investing.com/rss/bonds_Technical.rss",
"https://ca.investing.com/rss/bonds_Fundamental.rss",
"https://ca.investing.com/rss/news_11.rss",
"https://ca.investing.com/rss/market_overview_Technical.rss",
"https://ca.investing.com/rss/market_overview_Opinion.rss",
"https://ca.investing.com/rss/stock_Opinion.rss"
]
assert(len(RSS_FEED_GENERAL)==len(set(RSS_FEED_GENERAL)))

# For testing
# RSS_FEED_GENERAL = [
#     "https://www.globenewswire.com/RssFeed/subjectcode/21-Initial%20Public%20Offerings/feedTitle/GlobeNewswire%20-%20Initial%20Public%20Offerings",
# "https://www.globenewswire.com/RssFeed/subjectcode/27-Mergers%20And%20Acquisitions/feedTitle/GlobeNewswire%20-%20Mergers%20And%20Acquisitions",
# "https://www.globenewswire.com/RssFeed/subjectcode/72-Press%20Releases/feedTitle/GlobeNewswire%20-%20Press%20Releases",
# "https://www.globenewswire.com/RssFeed/orgclass/1/feedTitle/GlobeNewswire%20-%20News%20about%20Public%20Companies",
# "https://www.globenewswire.com/RssFeed/country/Canada/feedTitle/GlobeNewswire%20-%20News%20from%20Canada",
# "https://www.globenewswire.com/RssFeed/industry/4000-Health%20Care/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Health%20Care",
# "https://www.globenewswire.com/RssFeed/industry/1-Oil%2026%20Gas/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Oil%20and%20Gas",
# "https://www.globenewswire.com/RssFeed/industry/9000-Technology/feedTitle/GlobeNewswire%20-%20Industry%20News%20on%20Technology",
# "https://www.globenewswire.com/RssFeed/language/en/country/canada/industry/1/"
# ]
#



month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

day =['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

direction = ['north','west','east','south']
misc = ['manhattan','month','day','week','ceo','thing','things','yes','no','office','white collar watch','thousand','million','billion']
country = ['us','US','U S','UK','U K','europe','road','london','america']



# Twitter Users
TWITTER_INTERESTED = ['@McDonalds','@danielhowell']

#
# Reddit Scraper

SUBREDDIT_INTERESTED = ['Business','technology','entrepreneur','investing','businesshub','socialmedia',
                        'SecurityAnalysis','wallstreetbets','stockaday','StockMarket','algotrading','finance','stockmarket','investmentclub',
                        'CryptoCurrency','options','cryptocurrencies','Forex','Stock_Picks','RobinHood']

SUBREDDIT_INTERESTED = []
DAY_CUT =['Mon', 'Tu','Wed', 'Thur', 'Fri', 'Sat', 'Sun']


MIN_SUBMISSION_SCORE = 50
MAX_NUM_COMMENTS = 2
MIN_BODY_TITLE_LENGTH = 20
#

remove_if_present = ['trump','mueller','retirement']