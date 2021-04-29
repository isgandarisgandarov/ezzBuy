from ezzBuy.BusinessLayer.displayer import Displayer
from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.tapaz_scraper import TapazScraper


class TapazDisplayer(Displayer):
    def __init__(self, tapaz_scraper: Scraper):
        self.tapaz_scraper = tapaz_scraper

    def currency_converter(self, products, currency):
        if currency == 'usd':
            for dic in products:
                dic['price'] *= 0.59
                dic['price'] = round(dic['price'], 2)

    def display(self, product, sort, currency, min_price=0.0, max_price=100000.0):
        products = self.tapaz_scraper.scrape(product)
        self.currency_converter(products, currency)
        if min_price and max_price:
            products = self.min_max_filter(products, float(min_price), float(max_price))
        if sort == 'ascending':
            products = self.sort_by_price(products)
        elif sort == 'descending':
            products = self.sort_by_price(products, True)
        return products


tapaz = TapazScraper()
tapaz_displayer = TapazDisplayer(tapaz)

print(tapaz_displayer.display('keyboard', 'ascending', 'azn', 2, 1000))
print()
print(tapaz_displayer.display('monitor', 'ascending', 'azn', 2, 1000))

