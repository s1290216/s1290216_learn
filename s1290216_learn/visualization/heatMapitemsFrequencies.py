import plotly.express as px

class heatMapItemsFrequencies:
    def __init__(self, itemsFrequenciesDictionary):
        latitude = []
        longitude = []
        frequency = []
        for k, v in itemsFrequenciesDictionary.items():
            if ',' in k:
                points = k.split(',')
                for p in points:
                    long, lati = p.replace('Point(', '').replace(').1', '').replace(')', '').split()
                    latitude.append(float(lati))
                    longitude.append(float(long))
                    frequency.append(int(v))
            else:
                long, lati = k.replace('[\'Point(', '').replace(')\']', '').replace(').1\']', '').split()
                latitude.append(float(lati))
                longitude.append(float(long))
                frequency.append(int(v))
        figure = px.density_mapbox(
            lat = latitude,
            lon = longitude,
            z = frequency,
            size = frequency,
            radius = 10,
            center = {'lat': 34.686567, 'lon': 135.52000},
            zoom = 4,
            height = 600,
            width = 800
        )
        figure.update_layout(mapbox_style = 'open-street-map')
        figure.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
        figure.update_layout(title_text = "HeatMap")
        figure.show()

if __name__ == "__main__":
    heatMapItemsFrequencies(dictionary)