import duckdb
import os

def initialize_database():
    """Initialize the DuckDB database with spatial extension"""
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Connect to DuckDB database file
    conn = duckdb.connect('data/climate_biodiversity.duckdb')
    
    # Install and load spatial extension
    conn.install_extension('spatial')
    conn.load_extension('spatial')
    
    conn.sql("DROP TABLE IF EXISTS biodiversity")
    
    conn.sql("CREATE TABLE biodiversity (gbif_id BIGINT, scientific_name VARCHAR, country VARCHAR, latitude DOUBLE, longitude DOUBLE, year INTEGER, month INTEGER, day INTEGER, species VARCHAR, recordedBy VARCHAR)")
    
    print("Database initialized successfully!")
    conn.close()

if __name__ == "__main__":
    initialize_database()