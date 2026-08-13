
from pathlib import Path
import sqlite3
import pandas as pd

# Project root is one level above this file
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# File locations
csv_path = PROJECT_ROOT / "data" / "online_shoppers_intention.csv"
database_dir = PROJECT_ROOT / "database"
database_path = database_dir / "shoppers.db"

# Make sure the database folder exists
database_dir.mkdir(exist_ok=True)

# Load CSV
df = pd.read_csv(csv_path)

print(f"Loaded {len(df):,} rows from {csv_path.name}")

# Create SQLite database and table
with sqlite3.connect(database_path) as connection:
    df.to_sql(
        "sessions",
        connection,
        if_exists="replace",
        index=False
    )

print(f"Database created: {database_path}")
print("Table created: sessions")