import xarray as xr
import numpy as np
import zipfile
    
temperature_data = xr.open_dataset("data/extracted/temperature.nc")
precipitation_data = xr.open_dataset("data/extracted/precipitation.nc")

combined_data = xr.merge([temperature_data, precipitation_data])

print(combined_data)
print(combined_data.dims)
print(combined_data.coords)
print(combined_data.data_vars)
print(combined_data["t2m"])

combined_data["t2m"].plot()