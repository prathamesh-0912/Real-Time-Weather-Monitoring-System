import xarray as xr

def getdatahourly(variable, start_date, end_date):
        if variable == 'Temperature':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\TEMP\\6-Hourly-temperature_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['TMP_L100']
        elif variable == 'Geopotential Height':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\GPH\\6-Hourly_geopotentialheight_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['HGT_L100']
        elif variable == 'Precipitable Water':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\PPW\\6-Hourly_ppw_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['P_WAT_L200']
        elif variable == 'U Component of Wind':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\UCOW\\6-Hourly_UCOW_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['U_GRD_L100']
        elif variable == 'V Component of Wind':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\VCOW\\6-Hourly_VCOW_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['V_GRD_L100']  
        elif variable == 'Mean speed of Wind':
            xds_u = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\UCOW\\6-Hourly_UCOW_data.nc', parallel=False)
            xds_v = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\VCOW\\6-Hourly_VCOW_data.nc', parallel=False)

            # Select data for the given date range
            xds_u = xds_u.sel(time=slice(start_date, end_date))
            xds_v = xds_v.sel(time=slice(start_date, end_date))
        
            # Calculate wind speed
            data = (xds_u['U_GRD_L100'] ** 2 + xds_v['V_GRD_L100'] ** 2) ** 0.5


        elif variable == 'Mean Sea Level Pressure':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\MSLP\\6-Hourly_MSLP_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['PRES_L101'] 
        elif variable == 'Tropospheric Temperature':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\TEMP\\6-Hourly-temperature_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['TMP_L100']
        elif variable == 'Tropospheric Thickness':
            xds = xr.open_mfdataset('C:\\Users\\lawan\\OneDrive\\Documents\\Pranjal\\New folder\\data\\GPH\\6-Hourly_geopotentialheight_data.nc', parallel=False)
            data = xds.sel(time=slice(start_date, end_date))['HGT_L100']
        
        return data