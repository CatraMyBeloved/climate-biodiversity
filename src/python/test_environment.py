import sys
import pandas as pd
import numpy as np
import duckdb

# Print Python version and location
print(f"Python version: {sys.version}")
print(f"Python location: {sys.executable}")

# Test key packages
print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print(f"duckdb version: {duckdb.__version__}")

# Test DuckDB connection
try:
    conn = duckdb.connect(':memory:')
    conn.execute("CREATE TABLE test (id INTEGER, name VARCHAR)")
    conn.execute("INSERT INTO test VALUES (1, 'Environment Test')")
    result = conn.execute("SELECT * FROM test").fetchall()
    print(f"DuckDB test result: {result}")
    conn.close()
    print("DuckDB connection test successful!")
except Exception as e:
    print(f"DuckDB connection test failed: {str(e)}")