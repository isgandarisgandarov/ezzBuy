from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def aliexpressScraper(product):
    if product == '':
        return []
    url = f'https://aliexpress.ru/wholesale?catId=0&SearchText={product}'

    chromeOptions = Options()
    chromeOptions.headless = False
    driver = webdriver.Chrome(executable_path='C:\\Webdriver\\bin\\chromedriver.exe', options=chromeOptions)
    driver.get(url)
    sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find_all('div', 'product-card')

    def scrapeInfo(item):
        try:
            link = item.a.get('href')
        except AttributeError:
            link = ""
        try:
            title = item.find('a', 'item-title').get('title').strip()
        except AttributeError:
            title = 'No title provided'
        try:
            price = item.find('span', 'price-current').text.strip()
            price = price.encode('ascii', 'replace')
        except AttributeError:
            price = 0
        try:
            rating = item.find('span', 'rating-value').text.strip()
        except AttributeError:
            rating = 'No rating provided'

        result = {'title': title,
                  'price': price,
                  'rating': rating,
                  'link': link,
                  'source': 'aliexpress.ru'}
        return result

    products = []
    for item in results:
        record = scrapeInfo(item)
        if record:
            products.append(record)

    driver.quit()
    return products


# print(aliexpressScraper('keyboard'))