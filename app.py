from flask import Flask, render_template, url_for, request
from amazon_scraper import scraper

app = Flask(__name__)
app.config['SECRET_KEY'] = '34806b7e050652f3fc730b3fbc22d0ee'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form['search']
        products = scraper(item)
        return render_template('index.html', products=products)
    else:
        products = []
        return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
