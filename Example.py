import praw
from praw.models import MoreComments
import csv
import re


reddit = praw.Reddit(client_id='X01Xd6HhB1xY0w',
                     client_secret='BjbKTcZtNxEf6RNZ21HEREtqdbg',
                     password='Thisisapassword!',
                     user_agent='testscript by /u/fakebot3',
                     username='vancouver_sub100')



#'Hotwife'
comment_subreddit = []

def clean_value(val):
    return ('mod' not in val ) and ('vote' not in val) and ('flag' not in val) and ('bot' not in val)

def scrape_comments():
    with open(r'C:\Users\Dan\Desktop\all.txt', 'a', encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file, delimiter=',')

        for sub_red in comment_subreddit:
            print(sub_red)

            subreddit = reddit.subreddit(sub_red)
            collector = []

            for submission in subreddit.top(limit=300, time_filter='month'):
                collector.append(submission.title)
                for top_level_comment in submission.comments:
                    if isinstance(top_level_comment, MoreComments):
                        continue

                    value = top_level_comment.body.strip()
                    value = re.sub('[\W_]+', ' ', value)
                    if clean_value(value):
                        collector.append(value)
                    if len(collector)>100:
                        writer.writerow(collector)
                        collector = []
                        #time.sleep(0.5)

            writer.writerow(collector)





scrape_comments()
