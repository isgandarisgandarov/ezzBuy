import requests, json
from ezzBuy.BusinessLayer.scraper import Scraper
from ezzBuy.BusinessLayer.config_parser import config


class AliexpressScraper(Scraper):
    @staticmethod
    def scrapeItem(item):
        title = item['product_title']
        price = item['app_sale_price']
        link = item['product_detail_url']
        source = 'aliexpress.com'
        currency = item['app_sale_price_currency']
        try:
            shipping = item['metadata']['logistics']['logisticsDesc']
            rating = item['evaluate_rate']
        except:
            shipping = ''
            rating = 'No rating provided'
        return {
            'title': title,
            'price': price,
            'rating': rating,
            'link': link,
            'source': source,
            'shipping': shipping,
            'currency': currency}

    def scrape(self, product):
        url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

        querystring = {"name": product, 'page': '1'}

        headers = {
            'x-rapidapi-key': "4b8f198acemsh3f250505b04fbd8p15736ajsndf9e45e323b6",
            'x-rapidapi-host': "magic-aliexpress1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(str(response.text))
        items = json_data['docs']
        products = []
        counter = 0

        for item in items:
            if counter >= int(config.get_property('SEARCH_NUMBER_ALIEXPRESS')):
                break
            record = self.scrapeItem(item)
            if record:
                products.append(record)
                counter += 1
        return products

