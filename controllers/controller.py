from flask import render_template
from app import app
from models.order_lists import orders

@app.route('/')
def index():
    
    return render_template("index.html", title="Home", orders=orders)

@app.route('/orders/<num>')
def order(num):
    return render_template("order.html", title="Order", order=orders[int(num)])
