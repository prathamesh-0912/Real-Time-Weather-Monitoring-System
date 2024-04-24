import os
import xarray as xr

def prepare_temperature_data(interval):
    if interval == "Daily":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\precipitableWater\\*.nc', parallel=False)
        xds_daily = xds.resample(time='1D').mean()
        return xds_daily['P_WAT_L200']
    elif interval == "6-Hourly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\precipitableWater\\*.nc', parallel=False)
        return xds['P_WAT_L200']
 
def save_temperature_data(interval, folder_path):
    temperature_data = prepare_temperature_data(interval)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'Daily_ppw_data.nc')
    temperature_data.to_netcdf(file_path)

if __name__ == '__main__':
    folder_path = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\PPW'
    save_temperature_data("Daily", folder_path)
 