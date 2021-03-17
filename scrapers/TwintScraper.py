import twint
import os

from models.IndexAccount import IndexAccount
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
class TwintScraper:
    def __init__(self):
        pass

    def scrap_one_iteration_index(self, account: IndexAccount):
        date_to = account.last_date
        self.basepath = 'data/accounts/' + account.scraper_id + "/"
        date_since = date_to - relativedelta(months=1)

        since = date_since.strftime("%Y-%m-%d")
        until = date_to.strftime("%Y-%m-%d")
        self.scrap_account_period(account.account, since,until)

    def scrap_account_period(self, account, since, until):
        c = twint.Config()
        if ("#" in account):
            c.Search = account
        else:
            print(account)
            c.Username = account
        lang = os.getenv("lang")
        if not lang == None and not lang == "":
            print("lang set")
            c.Lang = lang

        near = os.getenv("near")
        if not near == None and not near == "":
            print("near set", near)
            c.Near = near

        c.Store_csv = True
        filename = account + "_" + str(since) +"---" +str(until) +  ".csv"
        path = self.basepath + account
        c.Output = path + '/' + filename
        #c.Since = '2018-10-01'
        c.Since = since
        c.Until = until

        self.ensure_path_data_exists(account)
        twint.run.Search(c)

    def ensure_path_data_exists(self, account):

        if not os.path.exists('data/accounts/'):
            os.makedirs('data/accounts/')

        if not os.path.exists(self.basepath):
            os.makedirs(self.basepath)

        if not os.path.exists(self.basepath+account):
            os.makedirs(self.basepath+account)
