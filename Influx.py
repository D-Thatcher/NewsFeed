import RSSParser
import TwitterParser
import RedditParser
import Util


class News:
    def __init__(self):
        self.twitter_feed = TwitterParser.TwitterParser()
        self.reddit_feed = RedditParser.RedditParser()

        self.include_reddit = True
        self.include_twitter = True


    def renew_twitter(self):
        self.twitter_feed = TwitterParser.TwitterParser()

    def renew_reddit(self):
        self.reddit_feed = RedditParser.RedditParser()

    def _sort_all_item(self,lo_item):
        sorted_entries = sorted(lo_item, key=lambda entry: entry["published_parsed"])
        sorted_entries.reverse()  # for most recent entries first
        return sorted_entries

    def rss_items(self,rss_urls):
        try:
            return RSSParser.get_feed(rss_urls)

        except Exception as e:
            print(repr(e))
            print('__________________________________________________________________')
            print('Error in RSSParser')
            print('Connected to Internet: ',Util.internet_on())
            print('__________________________________________________________________')
            return []

    def twitter_items(self,twitter_users):
        try:
            return self.twitter_feed.scrape_all_user(twitter_users)

        except Exception as e:
            print(repr(e))
            print('__________________________________________________________________')
            print('Error in TwitterParser')
            # print('Connected to Twitter: ', self.twitter_feed.verify_active())
            print('Connected to Internet: ',Util.internet_on())
            print('__________________________________________________________________')
            return []

    def reddit_items(self,subreddit_names):
        try:
            return self.reddit_feed.scrape_all_subreddit(subreddit_names)
        except Exception as e:
            print(repr(e))
            print('__________________________________________________________________')
            print('Error in RedditParser')
            print('Connected to Reddit: ', '?')
            print('Connected to Internet: ', Util.internet_on())
            print('__________________________________________________________________')
            return []


    def update_information(self,rss_urls, twitter_users, subreddit_names):
        print('Gathering RSS Feed...')
        feed = self.rss_items(rss_urls)
        twitter_items = []
        reddit_items = []
        if self.include_twitter:
            print('Gathering Twitter Feed...')
            twitter_items = self.twitter_items(twitter_users)
            if len(twitter_items)==0:
                print('Empty twitter feed')
        if self.include_reddit:
            print('Gathering Reddit Feed...')
            reddit_items = self.reddit_items(subreddit_names)
            if len(reddit_items)==0:
                print('Empty Reddit feed')

        if len(feed) == 0:
            print('Empty RSS feed')

        return self._sort_all_item(feed+twitter_items+reddit_items)



