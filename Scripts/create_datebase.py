import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

conn = sqlite3.connect(BASE_DIR / "mutual_fund.db")

with open(BASE_DIR / "Scripts" / "create_tables.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

conn.commit()
conn.close()

print("Tables created successfully")