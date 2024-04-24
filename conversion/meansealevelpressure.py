import os
import xarray as xr

def prepare_temperature_data(interval):
    if interval == "Daily":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\meansealevelpressure\\*.nc', parallel=False)
        xds_daily = xds.resample(time='1D').mean()
        return xds_daily['PRES_L101'] 
    elif interval == "6-Hourly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\meansealevelpressure\\*.nc', parallel=False)
        return xds['PRES_L101'] 
    elif interval == "Yearly":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\meansealevelpressure\\*.nc', parallel=False)
        data  = xds.resample(time='YS').mean()
        return data['PRES_L101']
    elif interval == "seasonal":
        xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\meansealevelpressure\\*.nc', parallel=False)
        data  = xds.resample(time='4MS').mean()
        return data['PRES_L101']
 
def save_temperature_data(interval, folder_path):
    temperature_data = prepare_temperature_data(interval)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'seasonal_MSLP_data.nc')
    temperature_data.to_netcdf(file_path)

if __name__ == '__main__':
    folder_path = 'C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\MSLP'
    #save_temperature_data("Yearly", folder_path)
    #save_temperature_data("Daily", folder_path)
    save_temperature_data("seasonal", folder_path)
