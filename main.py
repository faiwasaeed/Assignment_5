from sqlalchemy import create_engine
import pandas as pd

# connection string
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/testdb"
)

# read data
df = pd.read_sql("SELECT * FROM orders", engine)

print(df.head())