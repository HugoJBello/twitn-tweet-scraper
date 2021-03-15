from models.IndexAccount import IndexAccount
from datetime import datetime, timedelta
from models.Config import Config
from scrapers.TwintScraper import TwintScraper
from dateutil.relativedelta import relativedelta

import time

class AccountScrapper:
    def __init__(self, config: Config):
        self.config = config
        self.scraping_id = config.scraping_id
        self.scraper = TwintScraper()
        self.accounts = []
        self.sleep_time_between_requests = 10
        for account_str in config.accounts:
            account = IndexAccount(account_str, self.scraping_id, config.scraper_type)
            account.get()
            self.accounts.append(account)
            print("_",account)

    def scrap_one_day_in_each_account(self):
        index = 0
        if (self.config.account_index > len(self.accounts)):
            self.config.account_index = 0
            self.config.update()
            
        print("starting process in url index " +str(self.config.account_index))

        while index < len(self.accounts):
            index = self.config.account_index
            account = self.accounts[index]
            self.scrap_one_iteration(account)
            index = index + 1
            self.config.account_index = index
            self.config.update()

        self.config.account_index = 0
        self.config.update()

    def scrap_one_iteration(self, account: IndexAccount):
        date_to = account.last_date
        date_since = date_to - timedelta(days=1)
        
        since = date_since.strftime("%Y-%m-%d")
        until = date_to.strftime("%Y-%m-%d")

        try:
            print("************************************************************")
            print("scraping " + account.account + " in period ", since,until)
            print("************************************************************")

            self.scraper.scrap_one_iteration_index(account)
            date_since = date_to - relativedelta(months=1)
            account.update_date(date_since)

        except:
            time.sleep(self.sleep_time_between_requests)
            print("retrying scraping " + account.account + " in period ", since,until)

        time.sleep(self.sleep_time_between_requests)

        

            


#tweetCriteria = got.manager.TweetCriteria().setUsername("realdonaldtrump").setMaxTweets(1)
#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

#print(tweet.__class__())