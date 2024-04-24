import xarray as xr
import pandas as pd

# Load the NetCDF file
data = xr.open_dataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\GPH\\geopotentialheight_seasonal_data.nc')

# Extract data for the specific location and pressure level
location_data = data.sel(lat=30, lon=100, method='nearest')
level_data = location_data.sel(level0=250, method='nearest')

# Convert the data to a pandas DataFrame
df = level_data.to_dataframe().reset_index()

# Export the data to Excel
df.to_excel('output.xlsx', index=False)
