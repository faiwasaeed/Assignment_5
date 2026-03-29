from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql+psycopg://postgres:1234@localhost:5432/testdb"
)

df = pd.read_sql("SELECT * FROM orders", engine)

print(df.head())