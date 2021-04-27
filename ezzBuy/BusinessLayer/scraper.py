import abc


class Scraper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def scrape(self, product):
        pass




