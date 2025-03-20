import duckdb
import pandas as pd

csv_file = "0019123-250310093411724.csv"
# Connect to database
conn = duckdb.connect('data/climate_biodiversity.duckdb')

# Define columns to load and mapping
columns_to_load = ['gbifID', 'scientificName', 'countryCode', 'decimalLatitude', 
                   'decimalLongitude', 'year', 'month', 'day', 'species', 'recordedBy']

column_mapping = {
    'gbifID': 'gbif_id',
    'scientificName': 'scientific_name',
    'countryCode': 'country',
    'decimalLatitude': 'latitude',
    'decimalLongitude': 'longitude',
    'year': 'year',
    'month': 'month',
    'day': 'day',
    'species': 'species',
    'recordedBy': 'recordedBy'  
}

# Process the data in chunks
for chunk in pd.read_csv('data/biodiversity/raw/' + csv_file,
                         chunksize=100000,
                         usecols=columns_to_load,
                         delimiter="\t",
                         low_memory=False):
    # Rename columns
    chunk = chunk.rename(columns=column_mapping)
    
    # Insert data
    conn.sql("""
    INSERT INTO biodiversity (
        gbif_id, scientific_name, country, latitude, longitude,
        year, month, day, species, "recordedBy"
    ) SELECT 
        gbif_id, scientific_name, country, latitude, longitude,
        year, month, day, species, "recordedBy" 
    FROM chunk
    """)

print("Data import completed!")
conn.close()
