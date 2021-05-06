from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper


class AliexpressDisplayer(Displayer):
    def __init__(self, aliexpress_scraper: Scraper):
        self.aliexpress_scraper = aliexpress_scraper

    def get_products(self, product):
        return self.aliexpress_scraper.scrape(product)

    def currency_converter(self, products, currency):
        if currency == 'azn':
            for dic in products:
                dic['price'] *= 1.7
                dic['price'] = round(dic['price'], 2)
                dic['currency'] = 'AZN'
