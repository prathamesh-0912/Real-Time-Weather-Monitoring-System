import matplotlib.pyplot as plt
import io
import base64

def plotting(data_at_location, variable, location_type, levels, start_latitude, end_latitude, start_longitude, end_longitude, latitude, longitude, customized_area):
        plt.figure(figsize=(11, 7))
        data_at_location.plot()
        plt.xlabel("Date")
        plt.ylabel(variable)
        average_value = data_at_location.mean().compute().item()
        plt.axhline(y=average_value, color='gray', linestyle='--', label='Average')
        if location_type=="Area":
            plt.title(f'{variable} at Level {levels} (hPa) at latitude from {start_latitude} to {end_latitude} and longitude from {start_longitude} to {end_longitude}')
        elif location_type =="Specific Location":
            plt.title(f'{variable} at Level {levels} (hPa) at latitude {latitude} and longitude {longitude}')
        elif location_type=="Customized Areas":
            plt.title(f'{variable} at Level {levels} (hPa) at {customized_area}')


        plot_io = io.BytesIO()
        plt.savefig(plot_io, format='png')
        plot_io.seek(0)

        plot_image_base64 = base64.b64encode(plot_io.read()).decode('utf-8')

        return plot_image_base64