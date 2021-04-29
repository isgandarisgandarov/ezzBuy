from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.tapaz_scraper import TapazScraper


class TapazDisplayer(Displayer):
    def __init__(self, tapaz_scraper: Scraper):
        self.tapaz_scraper = tapaz_scraper

    def sort_by_price(self, products, sort=False):
        return sorted(products, key=lambda k: k['price'], reverse=sort)

    def min_max_filter(self, products, min_price=0, max_price=100000):
        def condition(dic, min_price, max_price):
            return min_price < dic['price'] < max_price

        filtered = [d for d in products if condition(d, min_price, max_price)]
        return filtered

    def currency_converter(self, products, currency):
        if currency == 'usd':
            for dic in products:
                dic['price'] *= 0.59
                dic['price'] = round(dic['price'], 2)

    def display(self, product, sort, currency, min_price=0, max_price=100000):
        products = self.tapaz_scraper.scrape(product)
        self.currency_converter(products, currency)
        if min_price and max_price:
            products = self.min_max_filter(products, min_price, max_price)
        if sort == 'ascending':
            products = self.sort_by_price(products)
        elif sort == 'descending':
            products = self.sort_by_price(products,True)
        return products


tapaz = TapazScraper()
tapaz_displayer = TapazDisplayer(tapaz)
print(tapaz_displayer.display('keyboard', 'none', 'azn', 20, 60))
print()
print(tapaz_displayer.display('monitor', 'none', 'azn', 20, 60))



