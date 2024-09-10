import folium
from folium.plugins import HeatMap

def create_heatmap(data, prediction_column):
    data['latitude'] = -23.5505
    data['longitude'] = -46.6333
    
    heat_data = [
        [row['latitude'], row['longitude']] 
        for index, row in data.iterrows() 
        if row[prediction_column] == 1
    ]
    
    heatmap = folium.Map(location=[-23.5505, -46.6333], zoom_start=10)
    HeatMap(heat_data).add_to(heatmap)
    
    return heatmap