from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
  {
    'id': 1,
    'name': 'Karotten',
    'price': '5',
    'currency': 'Fr.',
    'unit': 'kg',
    'producer':'Tübach - Granwehr'
  },
    {
    'id': 2,
    'name': 'Erdbeeren',
    'price': '4',
    'currency': 'Fr.',
    'unit': '250g',
    'producer':'Gossau - Fust'
  },
    {
    'id': 3,
    'name': 'Salat',
    'price': '3',
    'currency': 'Fr.',
    'unit': 'Stück',
    'producer':'St.Gallen - Müller'
  }
]

DEPOTS = [
  {
    'id': 1,
    'name': 'Lachen Drogerie',
    'street_number': 4,
    'street': 'fff',
    'postcode': 9000,
    'city': 'St.Gallen'
  },
  {
    'id': 2,
    'name': 'Liva Natura',
    'street_number': 4,
    'street': 'fff',
    'postcode': 9000,
    'city': 'St.Gallen'
  },  
  {
    'id': 3,
    'name': 'Benevolpark',
    'street_number': 4,
    'street': 'fff',
    'postcode': 9000,
    'city': 'St.Gallen'
  }
]

AMOUNT = [1,2,3,4,5,6,7,8,9,10]

@app.route("/")
def hello_order():
  return render_template('home.html', 
                        products=PRODUCTS,
                        depots=DEPOTS,
                        amount=AMOUNT)

@app.route("/api/products")
def list_products():
  return jsonify(PRODUCTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
