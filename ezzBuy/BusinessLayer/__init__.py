from ezzBuy.BusinessLayer.tapaz_scraper import TapazScraper
from ezzBuy.BusinessLayer.amazon_scraper import AmazonScraper
from ezzBuy.BusinessLayer.tapaz_displayer import TapazDisplayer
from ezzBuy.BusinessLayer.amazon_displayer import AmazonDisplayer

tapaz = TapazScraper()
tapaz_displayer = TapazDisplayer(tapaz)
amazon = AmazonScraper()
amazon_displayer = AmazonDisplayer(amazon)

