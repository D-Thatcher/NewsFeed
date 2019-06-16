from praw import Reddit
import datetime
from API_KEYS import *
from Constants import SUBREDDIT_INTERESTED, DAY_CUT, MIN_BODY_TITLE_LENGTH,MAX_NUM_COMMENTS,MIN_SUBMISSION_SCORE,month_lst

format = "Thu, 18 Apr"


# Account for no internet exception, failed client secret exception, catch general exception, print it, and proceed without reddit
class RedditParser (Reddit):
    def __init__(self,client_id=reddit_client_id,client_secret=reddit_client_secret,user_agent=reddit_user_agent):

        super().__init__(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)


    def clean_value(self,val):
        return (' mod ' not in val) and (' vote ' not in val) and (' flag ' not in val) and (' bot ' not in val)

    def connected(self):
        return False

    def get_date(self,submission):
        time = submission.created
        d = datetime.datetime.fromtimestamp(time)
        return DAY_CUT[d.weekday()] + ", " + str(d.day) + " " + month_lst[d.month - 1], str(d), d.timetuple()

    def scrape_all_subreddit(self, lo_subreddit):
        all_items = []
        for sub_red in lo_subreddit:
            all_items += self.scrape_text_from_subreddit(sub_red)
        return all_items

    def scrape_text_from_subreddit(self, sub_red):
        subreddit = self.subreddit(sub_red)
        lo_item = []

        # Collect 6 candidates from 'Hot' and 'Top' sections of the subreddit
        supa_hot_combo = [i for i in subreddit.top(limit=3,time_filter='day')]
        for j in subreddit.hot(limit=3):
            supa_hot_combo.append(j)

        for submission in supa_hot_combo:
            sufficient_score = submission.score >= MIN_SUBMISSION_SCORE
            clean_text = self.clean_value(submission.title) and self.clean_value(submission.selftext)
            sufficient_size = len(submission.title+ submission.selftext)>=MIN_BODY_TITLE_LENGTH

            if sufficient_score and clean_text and sufficient_size:

                date_title, date_summary, pub_parsed = self.get_date(submission)
                item = {'title':submission.title,'published':date_title,
                        'full date':date_summary, 'published_parsed':pub_parsed,
                        'link':'https://www.reddit.com'+submission.permalink,'twitter':False,'reddit':True}

                full_text = submission.selftext.replace('\n',' ').strip() + " "

                top_level_comments = list(submission.comments)[:MAX_NUM_COMMENTS]

                for comment in top_level_comments:
                    if comment.score >= int(submission.score/float(5)) and self.clean_value(comment.body):
                        full_text+=comment.body.replace('\n',' ').strip()+" "

                item['summary'] = 'Reddit: '+full_text.strip()

                lo_item.append(item)

        return lo_item













