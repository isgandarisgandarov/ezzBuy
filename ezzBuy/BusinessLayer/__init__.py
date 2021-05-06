from ezzBuy.BusinessLayer.tapaz_scraper import TapazScraper
from ezzBuy.BusinessLayer.amazon_scraper import AmazonScraper
from ezzBuy.BusinessLayer.aliexpress_scraper import AliexpressScraper
from ezzBuy.BusinessLayer.tapaz_displayer import TapazDisplayer
from ezzBuy.BusinessLayer.amazon_displayer import AmazonDisplayer
from ezzBuy.BusinessLayer.aliexpress_displayer import AliexpressDisplayer
from ezzBuy.BusinessLayer.driver import Driver

driver = Driver(True)

tapaz = TapazScraper(driver)
tapaz_displayer = TapazDisplayer(tapaz)

amazon = AmazonScraper(driver)
amazon_displayer = AmazonDisplayer(amazon)

aliexpress = AliexpressScraper()
aliexpress_displayer = AliexpressDisplayer(aliexpress)
