from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_depots_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM depots"))
    depots = []
    for row in result.all():
      depots.append(row._mapping)
    return depots

def load_grouped_orders_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM grouped_orders"))
    grouped_orders = []
    for row in result.all():
      grouped_orders.append(row._mapping)
    return grouped_orders

def load_grouped_order_from_db(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM grouped_orders WHERE id = :val ")
    values = {"val": id}
    result = conn.execute(query, values)
    rows = result.all()
    print("rows", rows)
    list = []
    list = rows[0]._mapping
    return list


def add_order_to_db(grouped_order_id, order_data):
  with engine.connect() as conn:

    query = text(
      "INSERT INTO orders (grouped_order_id, first_name, email) VALUES (:grouped_order_id, :first_name, :email)"
    )

    values = {
      'grouped_order_id': grouped_order_id,
      'first_name': order_data['first_name'],
      'email': order_data['email']
    }

    result = conn.execute(query, values)
    
    return result


def add_ordered_products_to_db(grouped_orders_products_id):
  with engine.connect() as conn:

    query = text(
      "INSERT INTO ordered_products (grouped_orders_products_id, quantity, total_price, order_id) VALUES (:grouped_orders_products_id, :quantity, :total_price, :order_id)"
    )

    values = {
      'grouped_orders_products_id': grouped_orders_products_id,
      'quantity': ordered_product_data['quantity'],
      'total_price': order_data['total_price'],
      'order_id': ordered_product_data['order_id']
    }

    result = conn.execute(query, values)
    
    return result
