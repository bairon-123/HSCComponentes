import oracledb

# Inicia el cliente Oracle si estás en Windows
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_26")

try:
    connection = oracledb.connect(
        user="SYSTEM",
        password="Byron-1313",
        dsn="localhost:1521/XE"
    )
    print("✅ Conexión exitosa a Oracle")
    connection.close()
except oracledb.DatabaseError as e:
    print("❌ Error de conexión a Oracle:", e)