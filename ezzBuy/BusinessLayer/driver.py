from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ezzBuy.BusinessLayer.config_parser import config


class Driver:
    def __init__(self, headless):
        self.headless = headless
        self.options = Options()
        self.options.headless = self.headless
        self.options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(executable_path=config.get_property("PATH"), options=self.options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
