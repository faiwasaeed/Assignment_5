import pandas as pd
from adbc_driver_postgresql import dbapi

conn = dbapi.connect(
    "postgresql://postgres:1234@localhost:5432/testdb"
)

df = pd.read_sql("SELECT * FROM products", conn)

print(df.head())