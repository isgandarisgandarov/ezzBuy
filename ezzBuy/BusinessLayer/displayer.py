import abc


class Displayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def currency_converter(self, products, currency):
        pass

    @abc.abstractmethod
    def display(self, product, sort, currency, min_price, max_price):
        pass

    @staticmethod
    def sort_by_price(products, sort=False):
        return sorted(products, key=lambda k: k['price'], reverse=sort)

    @staticmethod
    def min_max_filter(products, min_price=0.0, max_price=100000.0):
        def condition(dic, min_price, max_price):
            return min_price < dic['price'] < max_price

        filtered = [d for d in products if condition(d, min_price, max_price)]
        return filtered
