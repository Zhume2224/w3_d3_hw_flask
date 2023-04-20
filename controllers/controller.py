from app import app #to make it run?
from flask import render_template,url_for # for view function 
from models.orders import orders


@app.route('/')
def index():
   return render_template('index.html',banana=orders) #now need to put bananas in html


@app.route('/orders/<int:index>') #index depends on the index of specific order
def order_page(index):
   i=index
   return render_template('order.html',apple=orders[i])
    #now need to put bananas in html
