import plotly.express as px

class heatMapItemsFrequencies:
    def __init__(self, itemsFrequenciesDictionary):
        latitude = []
        longitude = []
        frequency = []
        point = []
        for k, v in itemsFrequenciesDictionary.items():
            point.append(k.replace('[\'', '').replace('\']'))
            long, lati = k.replace('[\'Point(', '').replace(')\']', '').split()
            latitude.append(float(lati))
            longitude.append(float(long))
            frequency.append(int(v))
        figure = px.scatter_mapbox(
            lat = latitude,
            lon = longitude,
            hover_name = point,
            color = frequency,
            size = frequency,
            size_max = 30,
            opacity = 0.4,
            center = {'lat': 34.686567, 'lon': 135.52000},
            zoom = 4,
            height = 600,
            width = 800
        )
        figure.update_layout(mapbox_style = 'open-street-map')
        figure.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
        figure.update_layout(title_text = "HeatMap")
        figure.show()