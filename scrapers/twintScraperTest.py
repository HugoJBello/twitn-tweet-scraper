
import unittest
from scrapers.TwintScraper import TwintScraper
from models.IndexAccount import IndexAccount
import datetime

class TestTwinScraper(unittest.TestCase):

    def test_one_iteration(self):
        scraper = TwintScraper()
        index = IndexAccount("NBA", "id_test", "account")
        index.last_date = datetime.datetime.now()

        scraper.scrap_one_iteration_index(index)
        #self.assertEqual('foo'.upper(), 'FOO')