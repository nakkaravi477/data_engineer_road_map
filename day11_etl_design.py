import pandas as pd
import sqlalchemy as sa

def extract(engine_uri, query):
    engine = sa.create_engine(engine_uri)
    return pd.read_sql(query, engine)

def transform(df):
    df = df.drop_duplicates()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df = df[df['amount'] > 0]
    return df

def load(df, target_uri, table_name):
    engine = sa.create_engine(target_uri)
    df.to_sql(table_name, engine, if_exists='append', index=False)

if __name__ == "__main__":
    src = extract("mysql://user:pass@host/db", "SELECT * FROM orders WHERE dt = CURDATE()")
    clean = transform(src)
    load(clean, "postgresql://user:pass@host/warehouse", "fact_orders")
