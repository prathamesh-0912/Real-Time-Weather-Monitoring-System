import xarray as xr
import netCDF4 as nc

filepath = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\MSLP\\seasonal_MSLP_data.nc'
# Open the NetCDF file
ds = xr.open_dataset(filepath)

# Open the NetCDF file
with ds as file:
    # Get a list of all variable names in the file
    variable_names = file.variables.keys()

# Print the list of variable names
print(variable_names)

