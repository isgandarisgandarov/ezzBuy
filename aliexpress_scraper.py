from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

product='keyboard'
url = f'https://aliexpress.ru/wholesale?catId=0&SearchText={product}'

chromeOptions = Options()
chromeOptions.headless = False
driver = webdriver.Chrome(executable_path='C:\\Webdriver\\bin\\chromedriver.exe', options=chromeOptions)
driver.get(url)
sleep(1)

soup = BeautifulSoup(driver.page_source, 'lxml')
results = soup.find_all('li', {'class': 'list-item'})

