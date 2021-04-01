from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

product = 'iphone X'
url = f'https://amazon.com/s?k={product}'

driver = webdriver.Chrome('C:\\Webdriver\\bin\\chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
results = soup.find_all('div', {'data-component-type': 's-search-result'})


def scrape_info(item):
    try:
        title = item.h2.a.text.strip()
    except AttributeError:
        title = "No title provided"
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text.strip()
    except AttributeError:
        price = "No price provided"
    try:
        rating = item.i.text
    except AttributeError:
        rating = "No rating provided"

    result = {'title': title,
              'price': price,
              'rating': rating}
    return result


products = []
for item in results:
    record = scrape_info(item)
    if record:
        products.append(record)

driver.quit()
