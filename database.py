from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://frbqbicyh7cod7fj4n25:pscale_pw_hCDpD8vD51OB1x5YVJ5feUCNFgtGc6nsUHtEu0ye9hG@aws.connect.psdb.cloud/collective-orders?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
                }
              }           
)

with engine.connect() as conn:
  result = conn.execute(text("select * from depots"))
  firstresult=result.all()[0]
  print(firstresult)