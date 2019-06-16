from twitter import Api
from API_KEYS import *
from datetime import datetime

class TwitterParser(Api):

    def __init__(self,consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=twitter_access_token_key,
                      access_token_secret=twitter_access_token_secret):

        super().__init__(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

        self.max_status_per_user = 1

    def scrape_all_user(self,lo_user):
        user_text = []
        for user in lo_user:
            user_text += self.get_statuses(user)
        return user_text

    def connected(self):
        return False

    def verify_active(self):
        return self.VerifyCredentials()

    def to_published(self,twitter_created_date):
        s = twitter_created_date.split(' ')
        date_title = s[0]+', '+s[2]+' '+ s[1]
        dt = datetime.strptime(twitter_created_date, '%a %b %d %H:%M:%S %z %Y')
        return date_title,str(dt),dt.timetuple()


    def get_statuses(self,user):
        statuses = self.GetUserTimeline(screen_name=user, count=self.max_status_per_user)
        lo_item = []
        for s in statuses:
            sd = s.AsDict()
            # print(sd)
            # for i in sd:
            #     print(i, " ", sd[i])
            date_title,date_summary,pub_parsed = self.to_published(sd['created_at'])

            lnk = sd['urls']
            if len(lnk)>0:
                lnk = lnk[0]
                if 'expanded_url' in lnk:
                    lnk = lnk['expanded_url']
                else:
                    lnk = ""
            else:
                lnk=''

            item = {'title': sd['text'], 'summary':'Twitter:', 'published': date_title,
                    'full date': date_summary, 'published_parsed': pub_parsed,'link':lnk,'twitter':True,'reddit':False}
            lo_item.append(item)

        return lo_item

    def get_followers(self,user):
        return self.GetFollowers(screen_name=user)

    def get_following(self,user):
        return self.GetFriends(screen_name=user)




