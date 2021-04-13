import threading
try:
    import queue
except ImportError:
    import Queue as queue
from amazon_scraper import amazonScraper, sortByPrice, minMax
from tapaz_scraper import tapazScraper
from aliexpress_scraper import aliexpressScraper


def wrapper(func, arg, queue):
    queue.put(func(arg))


def display(item, sort, currency, amazon, tapaz, aliexpress, min_price=0, max_price=10000000):
    q1, q2, q3 = queue.Queue(), queue.Queue(), queue.Queue()
    amazon_products = []
    tapaz_products = []
    aliexpress_products = []

    if amazon == ['on'] and tapaz == ['on'] and aliexpress == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        x3 = threading.Thread(target=wrapper, args=(aliexpressScraper, item, q3)).start()
        amazon_products = q1.get()
        tapaz_products = q2.get()
        aliexpress_products = q3.get()
    elif tapaz == ['on'] and amazon == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        amazon_products = q1.get()
        tapaz_products = q2.get()
    elif tapaz == ['on'] and aliexpress == ['on']:
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        x3 = threading.Thread(target=wrapper, args=(aliexpressScraper, item, q3)).start()
        tapaz_products = q2.get()
        aliexpress_products = q3.get()
    elif amazon == ['on'] and aliexpress == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        x3 = threading.Thread(target=wrapper, args=(aliexpressScraper, item, q3)).start()
        amazon_products = q1.get()
        aliexpress_products = q3.get()
    elif amazon == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        amazon_products = q1.get()
    elif tapaz == ['on']:
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        tapaz_products = q2.get()
    elif aliexpress == ['on']:
        x3 = threading.Thread(target=wrapper, args=(aliexpressScraper, item, q3)).start()
        aliexpress_products = q3.get()

    if currency == 'usd':
        for dic in tapaz_products:
            dic['price'] *= 0.59
            dic['price'] = round(dic['price'], 2)
        for dic in aliexpress_products:
            dic['price'] *= 0.013
            dic['price'] = round(dic['price'], 2)
    elif currency == 'azn':
        for dic in amazon_products:
            dic['price'] *= 1.7
            dic['price'] = round(dic['price'], 2)
        for dic in aliexpress_products:
            dic['price'] *= 0.022
            dic['price'] = round(dic['price'], 2)

    if min_price and max_price:
        amazon_products = minMax(amazon_products, float(min_price), float(max_price))
        tapaz_products = minMax(tapaz_products, float(min_price), float(max_price))
    if sort == 'ascending':
        amazon_products = sortByPrice(amazon_products)
        tapaz_products = sortByPrice(tapaz_products)
    elif sort == 'descending':
        amazon_products = sortByPrice(amazon_products, True)
        tapaz_products = sortByPrice(tapaz_products, True)
    return amazon_products, tapaz_products, aliexpress_products

