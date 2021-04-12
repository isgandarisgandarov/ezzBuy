from flask import Flask, render_template, url_for, request
from displayer import display

app = Flask(__name__)
app.config['SECRET_KEY'] = '34806b7e050652f3fc730b3fbc22d0ee'


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        item = request.form['search']
        sort = request.form['sort']
        min_price = request.form['min']
        max_price = request.form['max']
        tapaz = request.form.getlist('tapaz')
        amazon = request.form.getlist('amazon')
        aliexpress = request.form.getlist('aliexpress')
        amazon_products, tapaz_products = display(item, sort, amazon, tapaz, aliexpress,  min_price, max_price)

        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products)
    else:
        amazon_products = []
        tapaz_products = []
        return render_template('index.html', amazon_products=amazon_products, tapaz_products=tapaz_products)


if __name__ == '__main__':
    app.run(debug=True)
