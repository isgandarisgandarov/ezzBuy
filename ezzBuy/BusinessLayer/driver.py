from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self, headless):
        self.headless = headless
        self.options = Options()
        self.options.headless = self.headless
        self.options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(executable_path='C:\\Webdriver\\bin\\chromedriver.exe', options=self.options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()