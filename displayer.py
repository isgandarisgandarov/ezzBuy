import threading
try:
    import queue
except ImportError:
    import Queue as queue
from amazon_scraper import amazonScraper, sortByPrice, minMax
from tapaz_scraper import tapazScraper


def wrapper(func, arg, queue):
    queue.put(func(arg))


def display(item, sort,  amazon, tapaz, aliexpress, min_price=0, max_price=10000000):
    q1, q2 = queue.Queue(), queue.Queue()
    amazon_products = []
    tapaz_products = []
    aliexpress_products = []
    if amazon == ['on'] and tapaz == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        amazon_products = q1.get()
        tapaz_products = q2.get()
    elif tapaz == ['on']:
        x2 = threading.Thread(target=wrapper, args=(tapazScraper, item, q2)).start()
        tapaz_products = q2.get()
    elif amazon == ['on']:
        x1 = threading.Thread(target=wrapper, args=(amazonScraper, item, q1)).start()
        amazon_products = q1.get()

    if min_price and max_price:
        amazon_products = minMax(amazon_products, float(min_price), float(max_price))
        tapaz_products = minMax(tapaz_products, float(min_price), float(max_price))
    if sort == 'ascending':
        amazon_products = sortByPrice(amazon_products)
        tapaz_products = sortByPrice(tapaz_products)
    elif sort == 'descending':
        amazon_products = sortByPrice(amazon_products, True)
        tapaz_products = sortByPrice(tapaz_products, True)
    return amazon_products, tapaz_products

