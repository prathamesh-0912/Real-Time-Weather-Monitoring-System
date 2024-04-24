import numpy as np
import re

location_mapping = {
    "Area": "Area",
    "Specific Location": "Specific Location",
    "Customized Areas": {
        "North Hemisphere": {"lat_range": (90, 0), "lon_range": (0, 357.5)},
        "South Hemisphere": {"lat_range": (0, -90), "lon_range": (0, 357.5)},
        "Equator": {"lat_range": (2.5, -2.5), "lon_range": (0, 357.5)},
        "North Pole": {"lat_range": (90, 85), "lon_range": (0, 357.5)},
        "South Pole": {"lat_range": (-85, -90), "lon_range": (0, 357.5)},
        "NSBT": {"lat_range": (40, 25), "lon_range": (0, 357.5)},
        "SSBT": {"lat_range": (-25, -45), "lon_range": (0, 357.5)},
        "Tibet": {"lat_range": (37.5, 27.5), "lon_range": (75, 85)},
        "West Tibet": {"lat_range": (37.5, 27.5), "lon_range": (55, 75)},
        "East Tibet": {"lat_range": (37.5, 27.5), "lon_range": (85, 105)},
    }
}


def dms_to_decimal(dms_str, direction):
    latitudes = np.arange(90, -90.1, -2.5)
    longitudes = np.arange(0, 360.1, 2.5)
    if dms_str is None:
        raise ValueError(f"Invalid {direction} format. Value is missing.")
    
    # Parse latitude or longitude in the format "DD-Direction"
    dms_pattern = r'(\d+(?:\.\d+)?)-([NSEW])'
    match = re.match(dms_pattern, dms_str)
    
    if match:
        degrees = float(match.group(1))
        dms_direction = match.group(2)
        
        if dms_direction in ['S']:
            degrees = -degrees
            idx = np.abs(latitudes - (degrees)).argmin()
        elif dms_direction in ['N']:
            idx = np.abs(latitudes - degrees).argmin()
        elif dms_direction in ['E']:
            idx = np.abs(longitudes - degrees).argmin()
        elif dms_direction in ['W']:
            idx = np.abs(longitudes - degrees).argmin()
        return idx
    else:
        raise ValueError(f"Invalid {dms_str} format. Use 'DD{direction}' format.")
    
def get_coordinates(area_name):
    latitudes = np.arange(90, -90.1, -2.5)
    longitudes = np.arange(0, 360.1, 2.5)
    lat_range = location_mapping['Customized Areas'][area_name]["lat_range"]
    lon_range = location_mapping['Customized Areas'][area_name]["lon_range"]
    start_lat, end_lat = lat_range
    start_lon, end_lon = lon_range
    start_lat_index  = np.abs(latitudes - start_lat).argmin()
    end_lat_index = np.abs(latitudes - end_lat).argmin()
    start_lon_index = np.abs(longitudes - start_lon).argmin()
    end_lon_index = np.abs(longitudes - end_lon).argmin()
    return start_lat_index, end_lat_index, start_lon_index, end_lon_index