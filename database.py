from sqlalchemy import create_engine, text, insert
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


def load_grouped_order_from_db(id):
  with engine.connect() as conn:
    print("id: ", id)
    print("type id: ", type(id))
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
    print("order_data", order_data)
    print("type order_data", type(order_data))

    query = text(
      "INSERT INTO orders (grouped_order_id, first_name, email) VALUES (:grouped_order_id, :first_name, :email)"
    )

    values = {
      'grouped_order_id': grouped_order_id,
      'first_name': order_data['first_name'],
      'email': order_data['email']
    }

    result = conn.execute(query, values)
    print("result: ", result)
    return result
