from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

product = 'playstation 4'
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
    except AttributeError:
        price = "No price provided"
    try:
        rating = item.i.text
    except AttributeError:
        rating = "No rating provided"

    result = {'title': title,
              'price': price,
              'rating': rating,
              'link': link}
    return result


products = []
for item in results:
    record = scrape_info(item)
    if record:
        products.append(record)

driver.quit()
