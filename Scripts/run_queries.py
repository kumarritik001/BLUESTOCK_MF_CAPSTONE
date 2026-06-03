from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "Data" / "db" / "bluestock_mf.db"
sql_path = BASE_DIR / "Sql" / "queries.sql"

conn = sqlite3.connect(db_path)

with open(sql_path, "r", encoding="utf-8") as f:
    sql_script = f.read()

queries = [q.strip() for q in sql_script.split(";") if q.strip()]

for i, query in enumerate(queries, start=1):
    print(f"\n{'='*50}")
    print(f"Query {i}")
    print(f"{'='*50}")

    try:
        df = pd.read_sql(query, conn)
        print(df.head(10))
    except Exception as e:
        print("Error:", e)

conn.close()