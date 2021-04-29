from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.amazon_scraper import AmazonScraper


class AmazonDisplayer(Displayer):
    def __init__(self, amazon_scraper: Scraper):
        self.amazon_scraper = amazon_scraper

    def sort_by_price(self, products, sort=False):
        return sorted(products, key=lambda k: k['price'], reverse=sort)

    def min_max_filter(self, products, min_price=0.0, max_price=100000.0):
        def condition(dic, min_price, max_price):
            return min_price < dic['price'] < max_price

        filtered = [d for d in products if condition(d, min_price, max_price)]
        return filtered

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


amazon = AmazonScraper()
amazon_displayer = AmazonDisplayer(amazon)

print(amazon_displayer.display('keyboard', 'ascending', 'azn', 20.5, 1000.8))
print()
print(amazon_displayer.display('monitor', 'ascending', 'azn', 20.5, 1000.8))

