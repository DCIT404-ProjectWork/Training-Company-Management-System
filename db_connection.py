import oracledb

def get_connection():
    dsn = oracledb.makedsn("localhost", "1521", service_name="xepdb1")
    connection = oracledb.connect(user="system", password="admin", dsn=dsn)
    return connection