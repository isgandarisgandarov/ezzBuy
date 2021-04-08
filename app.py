from flask import Flask, render_template, url_for, request
from amazon_scraper import scraper, sortByPrice, minMax

app = Flask(__name__)
app.config['SECRET_KEY'] = '34806b7e050652f3fc730b3fbc22d0ee'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form['search']
        sort = request.form['sort']
        min_price = request.form['min']
        max_price = request.form['max']
        products = scraper(item)
        if min_price and max_price:
            products = minMax(products, float(min_price), float(max_price))
        if sort == 'ascending':
            products = sortByPrice(products)
        elif sort == 'descending':
            products = sortByPrice(products, True)
        return render_template('index.html', products=products)
    else:
        products = []
        return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
