from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.driver import Driver
from ezzBuy.BusinessLayer.config_parser import config
from bs4 import BeautifulSoup


class AmazonScraper(Scraper):
    def __init__(self, driver: Driver):
        self.driver = driver.get_driver()

    @staticmethod
    def get_url(product):
        template = 'https://www.amazon.com/s?k={}'
        product = product.replace(" ", "+")
        url = template.format(product)
        url += '&page={}'
        return url

    @staticmethod
    def scrape_item(item):
        try:
            atag = item.h2.a
            title = atag.text.strip()
            link = 'https://amazon.com' + atag.get('href')
        except AttributeError:
            title = "No title provided"
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text.strip()
            price = float(price[1:].replace(',', ''))
        except AttributeError:
            price = 0
        try:
            rating = item.i.text
        except AttributeError:
            rating = "No rating provided"

        return {'title': title,
                'price': price,
                'rating': rating,
                'link': link,
                'source': 'amazon.com',
                'currency': 'USD'}

    def scrape(self, product):
        products = []
        url = self.get_url(product)

        for page in range(1, 21):
            self.driver.get(url.format(page))
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})

            for item in results:
                record = self.scrape_item(item)
                if record['price'] == 0:
                    continue
                elif len(products) >= int(config.get_property('SEARCH_NUMBER_AMAZON')):
                    break
                else:
                    products.append(record)
            if len(products) >= int(config.get_property('SEARCH_NUMBER_AMAZON')):
                break
        return products
