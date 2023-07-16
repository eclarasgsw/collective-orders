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


def load_grouped_order_from_db():
  with engine.connect() as conn:
    print("id: ", type(id))
    result = conn.execute(text("SELECT * FROM grouped_orders WHERE id = 103 "))
    rows = result.all()
    print("rows", rows)
    print("type rows", type(rows))
    list = []
    list = rows[0]._mapping
    print("list: ", list)
    print("type list: ", type(list))
    return list


#def add_order_to_db(id, data):
#  return jsonify(data)

# with engine.connect() as conn:
#  query = text(
#   "INSERT INTO orders (grouped_order_id) VALUES (:1)"
#)

#conn.execute(query,
#            grouped_order_id=id
#          )
