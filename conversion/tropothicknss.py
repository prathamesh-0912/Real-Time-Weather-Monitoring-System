import os
import xarray as xr
import pandas as pd

def prepare_temperature_data(interval):
    if interval == "Daily":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\geopotentialHeight\\*.nc', parallel=False)
        xds_daily = xds.resample(time='1D').mean()
        return xds_daily['HGT_L100']
    elif interval == "6-Hourly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\geopotentialHeight\\*.nc', parallel=False)
        return xds['HGT_L100']
    elif interval == "Yearly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\geopotentialHeight\\*.nc', parallel=False)
        data  = xds.resample(time='YS').mean()
        return data['HGT_L100']
    elif interval == "Seasonal":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\geopotentialHeight\\*.nc', parallel=False)
        # Resample the data to get the mean for every four months
        data = xds.resample(time='4MS').mean()
        
        return data['HGT_L100']   
        

 
def save_temperature_data(interval, folder_path):
    temperature_data = prepare_temperature_data(interval)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'seasonal_GPH_data.nc')
    temperature_data.to_netcdf(file_path)

if __name__ == '__main__':
    folder_path = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\GPH'
    save_temperature_data("Seasonal", folder_path)
 