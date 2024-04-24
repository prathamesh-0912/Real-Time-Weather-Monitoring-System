import xarray as xr
import matplotlib.pyplot as plt

def plot_data_from_file(file_path, variable_name, year, season, level, lat, lon):
    # Open the NetCDF file using xarray
    try:
        data = xr.open_dataset(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error opening file: {e}")
        return
    
    # Access the variables
    try:
        variable_data = data[variable_name]
        forecast_hour_data = data['forecast_hour']
    except KeyError:
        print("One or more variables not found in the dataset.")
        return
    
    
    
    print(forecast_hour_data)
    # Select data for the specified coordinates
    try:
        selected_data = variable_data.sel(level0=level, lat=lat, lon=lon)
        forecast_data = forecast_hour_data.sel(year=year, season=season)
    except KeyError:
        print("One or more coordinates not found in the dataset.")
        return
    
    try:
        # Check if selected data has latitude and longitude dimensions
        if 'lat' in selected_data.dims and 'lon' in selected_data.dims:
            selected_data.plot(x='lon', y='lat')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.title(f'{variable_name} Data for Year {year}, Season {season}, Level {level}, Lat {lat}, Lon {lon}')
            plt.show()
        else:
            print("Selected data does not have latitude and longitude dimensions.")
    except TypeError as e:
        print(f"Error plotting data: {e}")

# Example usage:
file_path = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\GPH\\geopotentialheight_seasonal_data.nc'
variable_name = 'HGT_L100'
year = '2012'
season = 'Summer'
level = 1000
lat = 0
lon = 0

plot_data_from_file(file_path, variable_name, year, season, level, lat, lon)
