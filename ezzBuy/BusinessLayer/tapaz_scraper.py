from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.driver import Driver
from ezzBuy.BusinessLayer.config_parser import config
from bs4 import BeautifulSoup


class TapazScraper(Scraper):
    def __init__(self, driver: Driver):
        self.driver = driver.get_driver()

    @staticmethod
    def scrape_item(item):
        try:
            link = 'https://tap.az' + item.a.get('href')[:-9]
        except AttributeError:
            link = ""
        try:
            price = item.find('div', 'products-price').text.strip()
            price = float(price[:-3].replace(',', '').replace(' ', ''))
        except AttributeError:
            price = 0
        try:
            title = item.find('div', 'products-name').text.strip()
        except AttributeError:
            title = "No title provided"

        return {'title': title,
                'price': price,
                'link': link,
                'source': 'tap.az',
                'currency': 'AZN'}

    def scrape(self, product):
        url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={product}&q%5Bregion_id%5D='
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        results = soup.find_all('div', {'class': "products-i rounded"}) + soup.find_all('div', {
            'class': "products-i rounded bumped products-shop"}) + soup.find_all('div',
                                                                                 {'class': "products-i rounded bumped"})
        products = []
        counter = 0
        for item in results:
            if counter >= int(config.get_property('SEARCH_NUMBER_TAPAZ')):
                break
            record = self.scrape_item(item)
            if record:
                products.append(record)
            counter += 1
        return products
