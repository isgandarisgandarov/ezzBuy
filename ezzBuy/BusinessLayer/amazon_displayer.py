from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper


class AmazonDisplayer(Displayer):
    def __init__(self, amazon_scraper: Scraper):
        self.amazon_scraper = amazon_scraper

    def currency_converter(self, products, currency):
        if currency == 'azn':
            for dic in products:
                dic['price'] *= 1.7
                dic['price'] = round(dic['price'], 2)

    def display(self, product, sort, currency, min_price=0.0, max_price=100000.0):
        products = self.amazon_scraper.scrape(product)
        self.currency_converter(products, currency)
        if min_price and max_price:
            products = self.min_max_filter(products, float(min_price), float(max_price))
        if sort == 'ascending':
            products = self.sort_by_price(products)
        elif sort == 'descending':
            products = self.sort_by_price(products, True)
        return products

