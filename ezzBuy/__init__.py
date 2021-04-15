from flask import Flask
from ezzBuy.displayer import display

app = Flask(__name__)
app.config['SECRET_KEY'] = '34806b7e050652f3fc730b3fbc22d0ee'

from ezzBuy import routes
