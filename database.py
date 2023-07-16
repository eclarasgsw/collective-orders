from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_depots_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from depots"))
    depots = []
    for row in result.all():
      depots.append(row._mapping)
    return depots


def add_order_to_db(id, data):
  return jsonify(data)
  
 # with engine.connect() as conn:
  #  query = text(
   #   "INSERT INTO orders (grouped_order_id) VALUES (:1)"
    #)

  
    #conn.execute(query,
     #            grouped_order_id=id
      #          )
