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
    
    # Create example tables
    conn.execute("""
        CREATE TABLE IF NOT EXISTS climate_data (
            id INTEGER,
            date DATE,
            location VARCHAR,
            temperature FLOAT,
            precipitation FLOAT,
            geometry VARCHAR,  -- WKT format for spatial data
            PRIMARY KEY (id)
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS biodiversity_data (
            id INTEGER,
            species VARCHAR,
            observation_date DATE,
            location VARCHAR,
            count INTEGER,
            geometry VARCHAR,  -- WKT format for spatial data
            PRIMARY KEY (id)
        )
    """)
    
    print("Database initialized successfully!")
    conn.close()

if __name__ == "__main__":
    initialize_database()