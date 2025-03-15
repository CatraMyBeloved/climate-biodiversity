import duckdb
import os

def initialize_database():
    """Initialize the DuckDB database with spatial extension"""
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Connect to DuckDB database file
    conn = duckdb.connect('data/climate_biodiversity.duckdb')
    
    # Install and load spatial extension
    conn.execute("INSTALL spatial;")
    conn.execute("LOAD spatial;")
    
    print("Database initialized successfully!")
    conn.close()

if __name__ == "__main__":
    initialize_database()