import folium
from folium.plugins import HeatMap

def create_heatmap(data, prediction_column):
    # Adicionar coordenadas fixas para fins de exemplo
    # Essas coordenadas devem ser ajustadas conforme necessário
    data['latitude'] = -23.5505  # Latitude fixa para São Paulo
    data['longitude'] = -46.6333  # Longitude fixa para São Paulo
    
    # Filtrar dados para heatmap
    heat_data = [
        [row['latitude'], row['longitude']] 
        for index, row in data.iterrows() 
        if row[prediction_column] == 1
    ]
    
    # Criar o mapa
    heatmap = folium.Map(location=[-23.5505, -46.6333], zoom_start=10)
    HeatMap(heat_data).add_to(heatmap)
    
    return heatmap