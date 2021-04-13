from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def tapazScraper(product):
    if product == '':
        return []
    url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={product}&q%5Bregion_id%5D='

    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path='C:\\Webdriver\\bin\\chromedriver.exe', options=chromeOptions)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find_all('div', {'class': "products-i rounded"}) + soup.find_all('div', {'class': "products-i rounded bumped products-shop"})

    def scrapeInfo(item):
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

        result = {'title': title,
                  'price': price,
                  'link': link,
                  'source': 'tap.az'}
        return result

    products = []
    for item in results:
        record = scrapeInfo(item)
        if record:
            products.append(record)

    driver.quit()
    return products
