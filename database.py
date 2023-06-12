from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ivuv53np1py6mefv2u8e:pscale_pw_rqZ0qCnUa44q7LqSO8JmMmTcon9Oy31u59Ys6bLbI3w@aws.connect.psdb.cloud/collective-orders?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
                }
              }           
)

with engine.connect() as conn:
  result=conn.execute(text("select * from depots"))
  print(result.all())