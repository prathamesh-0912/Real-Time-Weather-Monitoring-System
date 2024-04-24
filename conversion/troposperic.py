import os
import xarray as xr

def prepare_temperature_data(interval):
    if interval == "Daily":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\temperature\\*.nc', parallel=False)
        xds_daily = xds.resample(time='1D').mean()
        return xds_daily['TMP_L100'] - 273.15
    elif interval == "6-Hourly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\temperature\\*.nc', parallel=False)
        return xds['TMP_L100'] - 273.15
    elif interval == "Yearly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\temperature\\*.nc', parallel=False)
        data  = xds.resample(time='YS').mean()
        return data['TMP_L100'] - 273.15
    elif interval == "Seasonal":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\temperature\\*.nc', parallel=False)
        data = xds.resample(time='4MS').mean()
        return data['TMP_L100']-273.15
 
def save_temperature_data(interval, folder_path):
    temperature_data = prepare_temperature_data(interval)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'seasonal_temperature_data.nc')
    temperature_data.to_netcdf(file_path)

if __name__ == '__main__':
    folder_path = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\TEMP'
    save_temperature_data("Seasonal", folder_path)
