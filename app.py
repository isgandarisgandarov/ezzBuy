from flask import Flask, render_template, url_for, request
from amazon_scraper import amazonScraper, sortByPrice, minMax
from tapaz_scraper import tapazScraper

app = Flask(__name__)
app.config['SECRET_KEY'] = '34806b7e050652f3fc730b3fbc22d0ee'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form['search']
        sort = request.form['sort']
        min_price = request.form['min']
        max_price = request.form['max']
        amazon_products = amazonScraper(item)
        tapaz_products = tapazScraper(item)
        if min_price and max_price:
            amazon_products = minMax(amazon_products, float(min_price), float(max_price))
            tapaz_products = minMax(tapaz_products, float(min_price), float(max_price))
        if sort == 'ascending':
            amazon_products = sortByPrice(amazon_products)
            tapaz_products = sortByPrice(tapaz_products)
        elif sort == 'descending':
            amazon_products = sortByPrice(amazon_products, True)
            tapaz_products = sortByPrice(tapaz_products, True)
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products)
    else:
        amazon_products = []
        tapaz_products = []
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products)


if __name__ == '__main__':
    app.run(debug=True)
