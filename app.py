from flask import Flask, render_template, jsonify, request
from database import load_depots_from_db #, add_order_to_db

app = Flask(__name__)

PRODUCTS = [{
  'id': 1,
  'name': 'Karotten',
  'pricePerUnit': 5,
  'currency': 'Fr.',
  'unit': '1 kg',
  'producer': 'Tübach - Granwehr'
}, {
  'id': 2,
  'name': 'Erdbeeren',
  'pricePerUnit': 4,
  'currency': 'Fr.',
  'unit': '250 g',
  'producer': 'Gossau - Fust'
}, {
  'id': 3,
  'name': 'Salat',
  'pricePerUnit': 3,
  'currency': 'Fr.',
  'unit': 'Stück',
  'producer': 'St.Gallen - Müller'
}]

GROUPED_ORDERS = [{
  'id': 1,
  'name':'2023-11-16 - Erdbeeren rot - 250 g',
  'date_delivery':'2023-11-16'
}, {
  'id': 2,
  'name':''
}, {
  'id': 3,
  'name':''
}]

GROUPED_ORDERS_PRODUCTS = [{
  'id':1,
  'product_id': 2,
  'product_name':'Erdbeeren',          #to delete
  'product_price': 4,                  
  'currency': 'Fr.',                  #to delete
  'product_unit': '250 g',             #to delete
  'product_producer':'Gossau - Fust',  #to delete
  'max_quantity':10,
  'total_outgoing':3,
  'in_stock':7,
  'grouped_order_id': 1,
}]

#GROUPED_ORDERS_PRODUCTS, Quantity
SHOPPING_CART=[]

ORDERED_PRODUCTS = [{
  'id':1,
  'grouped_orders_product_id': 1,
#  'productPrice': 5,
  'quantity': 3,
  'total_price': 15,
  'currency': 'Fr.'
}]

ORDERS = []

QUANTITY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@app.route("/")
def home():
  return render_template('home.html', grouped_orders=GROUPED_ORDERS)

#individual grouped order forms
@app.route("/order/<orderId>")
def order(orderId, quantity={}):
  depots = load_depots_from_db()
  #total_price = 0
  #for cart_product in CART_PRODUCTS:
  #  total_price += productPrice * quantity

  return render_template('order.html',
                         grouped_orders=GROUPED_ORDERS,
                         grouped_orders_products=GROUPED_ORDERS_PRODUCTS,
                         depots=depots,
                         quantity=QUANTITY,
                         orderId=orderId)

#API products old
@app.route("/api/products")
def list_products():
  return jsonify(PRODUCTS)

#Send order to database
@app.route("/order/<int:id>/create", methods=['post'])
def placeOrder(id):
  data = request.form
  grouped_order = GROUPED_ORDERS[id-1]
  
#  #add_order_to_db(id, data)
  return render_template('order_submitted.html', 
                         order=data, 
                         grouped_order=grouped_order)

#Exemple from Jovian Job
'''@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)'''


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
