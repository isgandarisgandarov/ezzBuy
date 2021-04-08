from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def scraper(product):
    if product == '':
        return []
    url = f'https://amazon.com/s?k={product}'

    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path='C:\\Webdriver\\bin\\chromedriver.exe', options=chromeOptions)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    def scrape_info(item):
        try:
            atag = item.h2.a
            title = atag.text.strip()
            link = 'https://amazon.com' + atag.get('href')
        except AttributeError:
            title = "No title provided"
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text.strip()
            price = float(price[1:])
        except AttributeError:
            price = 0
        try:
            rating = item.i.text
        except AttributeError:
            rating = "No rating provided"

        result = {'title': title,
                  'price': price,
                  'rating': rating,
                  'link': link,
                  'source': 'amazon.com'}
        return result


    products = []
    for item in results:
        record = scrape_info(item)
        if record:
            products.append(record)

    driver.quit()
    return products


def sortByPrice(products, order=False):
    return sorted(products, key=lambda k: k['price'], reverse=order)


def minMax(products, min_price, max_price):
    def condition(dic, min_price, max_price):
        return min_price < dic['price'] < max_price

    filtered = [d for d in products if condition(d, min_price, max_price)]
    return filtered


# items = scraper('playstation 5')
#
# print(minMax(items, 69, 100))
