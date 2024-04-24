from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from locationtype import getdataforarea, getdataforCA, getdataforSL
from levels import getlevel
from getdatadaily import getdatadaily
from getdatahourly import getdatahourly
from getdatayearly import getdatayearly
from getdataseasonal import getdataseasonal
from plot import plotting

level_mapping = {
    '1000': 1, '925': 2, '850': 3, '700': 4, '600': 5, '500': 6, '400': 7,
    '300': 8, '250': 9, '200': 10, '150': 11, '100': 12
}

variable_mapping = {
    'Temperature': 'Temperature' ,  
    'Geopotential Height': 'Geopotential Height', 
    'Precipitable Water': 'Precipitable Water',
    'U Component of Wind' : 'U Component of Wind',
    'V Component of Wind' : 'V Component of Wind',
    'Mean speed of Wind' : 'Mean speed of Wind',
    'Mean Sea Level Pressure' : 'Mean Sea Level Pressure',
    'Tropospheric Temperature' : 'Troposperic Temperature',
    'Tropospheric Thickness' : 'Tropospheric Thickness',
}

interval_mapping = {
    "6-Hourly": "6-Hourly",
    "Daily" : "Daily",
    "Yearly" : "Yearly",
    "Seasonal" : "Seasonal" 
}

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

app = Flask(__name__)


def plot_data(selected_level, level_type, start_level, end_level,  upper_level, lower_level, location_type, customized_area,  latitude, longitude, start_latitude, start_longitude,end_latitude, end_longitude, start_date, end_date, variable, interval):   
    if interval=="Daily":
        data = getdatadaily(variable, start_date, end_date)
    elif interval=="6-Hourly":
        data = getdatahourly(variable, start_date, end_date)
    elif interval=="Yearly":
        data = getdatayearly(variable, start_date, end_date)
    elif interval=="Seasonal":
        data = getdataseasonal(variable, start_date, end_date)
    
    index_level, index_level1, index_level2, levels = getlevel(variable, level_type, selected_level, upper_level, lower_level, start_level, end_level)

    try:
        if location_type=="Area":
            data_at_location = getdataforarea(data, variable, level_type, index_level, index_level1, index_level2, start_latitude, end_latitude, start_longitude, end_longitude)
            #plt.title(f'{variable} at Level {levels} (hPa) at latitude from {start_latitude} to {end_latitude} and longitude from {start_longitude} to {end_longitude}')
        elif location_type =="Specific Location":
            data_at_location = getdataforSL(data, variable, level_type, index_level, index_level1, index_level2, latitude, longitude)
            #plt.title(f'{variable} at Level {levels} (hPa) at latitude {latitude} and longitude {longitude}')
        elif location_type=="Customized Areas":
            data_at_location = getdataforCA(data, variable, level_type, index_level, index_level1, index_level2, customized_area)
            
        plot_image_base64 = plotting(data_at_location, variable, location_type, levels, start_latitude, end_latitude, start_longitude, end_longitude, latitude, longitude, customized_area)
        return plot_image_base64
        
    except ValueError as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_level = request.form.get('level')
        level_type = request.form.get('level_type')
        start_level = request.form.get('start_level')
        end_level = request.form.get('end_level')
        upper_level = request.form.get('upper_level')
        lower_level = request.form.get('lower_level')
        location_type = request.form.get('location')
        customized_area = request.form.get('custom_area')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        start_latitude = request.form.get('start_latitude')
        start_longitude = request.form.get('start_longitude')
        end_latitude = request.form.get('end_latitude')
        end_longitude = request.form.get('end_longitude')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        variable = request.form.get('variable')
        interval = request.form.get('interval')

        if variable in variable_mapping :
            plot_image = plot_data(selected_level, level_type, start_level, end_level, upper_level, lower_level, location_type, customized_area, latitude, longitude, start_latitude, start_longitude,end_latitude, end_longitude, start_date, end_date, variable, interval)            
            return render_template('index.html', levels=list(level_mapping.keys()), plot_image=plot_image, variables=list(variable_mapping.keys()), intervals=list(interval_mapping.keys()), locations=list(location_mapping.keys()), customized_areas=list(location_mapping['Customized Areas'].keys()))
        else:
            error_message = "Invalid input. Please enter valid latitude, longitude, start date, end date, and level."
            return render_template('index.html', levels=list(level_mapping.keys()), error_message=error_message, variables=list(variable_mapping.keys()), intervals=list(interval_mapping.keys()), locations=list(location_mapping.keys()), customized_areas=list(location_mapping['Customized Areas'].keys()))

    return render_template('index.html', levels=list(level_mapping.keys()), variables=list(variable_mapping.keys()), intervals=list(interval_mapping.keys()), locations=list(location_mapping.keys()), customized_areas=list(location_mapping['Customized Areas'].keys()))

if __name__ == '__main__':
    app.run(debug=True)

