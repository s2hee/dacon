import pandas as pd
address = pd.read_excel("C:/Users/YJ/Downloads/school_address.xlsx")

print(address.head(5))


#위도, 경도 리스트

x = []
y = []
for i in range(len(address['Latitude'])):
    if address['Latitude'][i] == 0.0 or address['Latitude'][i] == 0.0:
        pass
    else:

        x.append(address['Latitude'][i])
        y.append(address['Longitude'][i])

#지도

import folium
map_osm = folium.Map(location=[x[13],y[13]],zoom_start=14)
for i in range(len(x)):
    folium.Marker([x[i],y[i]], icon=folium.Icon(color='blue', icon='info-sign')).add_to(map_osm)

map_osm


