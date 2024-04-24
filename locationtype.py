from indexing import dms_to_decimal , get_coordinates

def getdataforarea(data, variable, level_type, index_level, index_level1, index_level2, start_latitude, end_latitude, start_longitude, end_longitude):
    start_lat_decimal = dms_to_decimal(start_latitude, 'N')
    end_lat_decimal = dms_to_decimal(end_latitude, 'N')
    start_lon_decimal = dms_to_decimal(start_longitude, 'E')
    end_lon_decimal = dms_to_decimal(end_longitude, 'E')
    start_lat_index = int(start_lat_decimal)
    start_lon_index = int(start_lon_decimal)
    end_lat_index = int(end_lat_decimal)
    end_lon_index = int(end_lon_decimal)
            
    if variable=="Tropospheric Temperature" or variable=="Tropospheric Thickness":
        data_square = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1))
        data_square = data_square.mean(dim='level0')
    elif variable=="Geopotential Height" and level_type=="multiple":
        data_start_level = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level1)
        data_end_level = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level2)

        data_square = data_end_level - data_start_level
    else:
        data_square = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level)
        if level_type=="multiple":
            data_at_location = data_at_location.mean(dim='level0')

    # Calculate the mean along latitude and longitude dimensions
    data_at_location = data_square.mean(dim=('lat', 'lon'))
    
    return data_at_location

def getdataforSL(data, variable, level_type, index_level, index_level1, index_level2, latitude, longitude):
    lat_decimal = dms_to_decimal(latitude, "N")
    lon_decimal = dms_to_decimal(longitude, 'E')
    lat_index = int(lat_decimal)
    lon_index = int(lon_decimal)
        
    if variable=="Tropospheric Temperature" or variable=="Tropospheric Thickness":
        data_square = data.isel(lat=lat_index, lon=lon_index)
        data_square = data_square.mean(dim='level0')
    elif variable=="Geopotential Height" and level_type=="multiple":
        data_start_level = data.isel(lat=lat_index, lon=lon_index, level0=index_level1)
        data_end_level = data.isel(lat=lat_index, lon=lon_index, level0=index_level2)
                
        data_square = data_start_level - data_end_level
    else:
        data_square = data.isel(lat=lat_index, lon=lon_index, level0=index_level)
        if level_type=="multiple":
            data_square = data_square.mean(dim='level0')
    return data_square
    
def getdataforCA(data, variable, level_type, index_level, index_level1, index_level2, customized_area):
    start_lat_decimal, end_lat_decimal, start_lon_decimal, end_lon_decimal = get_coordinates(customized_area)
    start_lat_index = int(start_lat_decimal)
    start_lon_index = int(start_lon_decimal)
    end_lat_index = int(end_lat_decimal)
    end_lon_index = int(end_lon_decimal)
            
    if variable=="Tropospheric Temperature" or variable=="Tropospheric Thickness":
        data_square = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1))
        data_square = data_square.mean(dim='level0')
    elif variable=="Geopotential Height" and level_type=="multiple":
        data_start_level = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level1)
        data_end_level = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level2)

        data_square = data_end_level - data_start_level
    else:
        data_square = data.isel(lat=slice(start_lat_index, end_lat_index + 1), lon=slice(start_lon_index, end_lon_index + 1), level0=index_level)
        if level_type=="multiple":
            data_at_location = data_square.mean(dim='level0')

            # Calculate the mean along latitude and longitude dimensions
    data_at_location = data_square.mean(dim=('lat', 'lon'))  
    
    return data_at_location 