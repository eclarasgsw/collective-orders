from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
  {
    'id': 1,
    'product_name': 'Karotten',
    'price': '5',
    'currency': 'Fr.',
    'unit': 'kg',
    'producer':'Tübach - Granwehr'
  },
    {
    'id': 2,
    'product_name': 'Erdbeeren',
    'price': '4',
    'currency': 'Fr.',
    'unit': '250g',
    'producer':'Gossau - Fust'
  },
    {
    'id': 3,
    'product_name': 'Salat',
    'price': '3',
    'currency': 'Fr.',
    'unit': 'Stück',
    'producer':'St.Gallen - Müller'
  }
]

@app.route("/")
def hello_order():
  return render_template('home.html', 
                         products=PRODUCTS)

@app.route("/api/products")
def list_products():
  return jsonify(PRODUCTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
