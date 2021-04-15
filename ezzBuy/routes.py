from flask import render_template, url_for, request
from ezzBuy.displayer import display
from ezzBuy import app


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form['search']
        sort = request.form['sort']
        currency = request.form['currency']
        min_price = request.form['min']
        max_price = request.form['max']
        tapaz = request.form.getlist('tapaz')
        amazon = request.form.getlist('amazon')
        aliexpress = request.form.getlist('aliexpress')
        amazon_products, tapaz_products, aliexpress_products = display(item, sort, currency, amazon, tapaz, aliexpress, min_price, max_price)

        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products, aliexpress_products=aliexpress_products)
    else:
        amazon_products = []
        tapaz_products = []
        aliexpress_products = []
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products, aliexpress_products=aliexpress_products)
