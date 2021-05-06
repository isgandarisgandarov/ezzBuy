import abc


class Displayer(metaclass=abc.ABCMeta):
    def display(self, product, sort, currency, min_price=0.0, max_price=100000.0):
        products = self.get_products(product)
        self.currency_converter(products, currency)
        if min_price and max_price:
            products = self.__min_max_filter(products, float(min_price), float(max_price))
        if sort == 'ascending':
            products = self.__sort_by_price(products)
        elif sort == 'descending':
            products = self.__sort_by_price(products, True)
        return products

    @abc.abstractmethod
    def get_products(self, product):
        pass

    @abc.abstractmethod
    def currency_converter(self, products, currency):
        pass

    @staticmethod
    def __sort_by_price(products, sort=False):
        return sorted(products, key=lambda k: k['price'], reverse=sort)

    @staticmethod
    def __min_max_filter(products, min_price=0.0, max_price=100000.0):
        def condition(dic, min_price, max_price):
            return min_price < dic['price'] < max_price
        filtered = [d for d in products if condition(d, min_price, max_price)]
        return filtered
