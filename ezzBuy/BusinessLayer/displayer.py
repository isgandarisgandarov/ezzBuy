import abc


class Displayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sort_by_price(self, products, sort):
        pass

    @abc.abstractmethod
    def min_max_filter(self, products, min_price=0, max_price=100000):
        pass

    @abc.abstractmethod
    def currency_converter(self, products, currency):
        pass
