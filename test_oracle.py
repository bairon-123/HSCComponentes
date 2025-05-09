import oracledb

# Ruta al Instant Client
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_26")

# Crear el DSN
dsn = oracledb.makedsn("localhost", 1521, service_name="xe")

try:
    connection = oracledb.connect(
        user="C##HSCcomp",
        password="hsccomp",
        dsn=dsn
    )
    print("✅ Conexión exitosa a Oracle!")
    connection.close()
except Exception as e:
    print("❌ Error de conexión:")
    print(e)