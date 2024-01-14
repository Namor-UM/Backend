import pandas as pd

def get_table(conn, table):
    return pd.read_sql(f"SELECT * FROM {table}", conn)


