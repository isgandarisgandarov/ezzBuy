from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper


class TapazDisplayer(Displayer):
    def __init__(self, tapaz_scraper: Scraper):
        self.tapaz_scraper = tapaz_scraper

    def get_products(self, product):
        return self.tapaz_scraper.scrape(product)

    def currency_converter(self, products, currency):
        if currency == 'usd':
            for dic in products:
                dic['price'] *= 0.59
                dic['price'] = round(dic['price'], 2)
                dic['currency'] = 'USD'
