from flask import render_template, url_for, request
from ezzBuy.BusinessLayer import tapaz_displayer
from ezzBuy.BusinessLayer import amazon_displayer
from ezzBuy import app


@app.route('/', methods=['GET', 'POST'])
def home():
    amazon_products = []
    tapaz_products = []
    aliexpress_products = []
    if request.method == 'POST':
        item = request.form['search']
        sort = request.form['sort']
        currency = request.form['currency']
        min_price = request.form['min']
        max_price = request.form['max']
        tapaz = request.form.getlist('tapaz')
        amazon = request.form.getlist('amazon')
        aliexpress = request.form.getlist('aliexpress')
        if amazon == ['on']:
            amazon_products = amazon_displayer.display(item, sort, currency, min_price, max_price)
        if tapaz == ['on']:
            tapaz_products = tapaz_displayer.display(item, sort, currency, min_price, max_price)
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products, aliexpress_products=aliexpress_products)
    else:
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products, aliexpress_products=aliexpress_products)
