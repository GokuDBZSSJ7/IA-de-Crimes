from preprocessamente import load_and_preprocess_data
from modelo import train_model
from visualize import create_heatmap
import webbrowser
import os

if __name__ == "__main__":
    data = load_and_preprocess_data('../dados/crimes.csv')
    
    model = train_model(data)
    
    features = data[['ano', 'mes', 'id_municipio', 'latrocinio']].dropna()
    
    features = features.loc[data['homicidio_doloso'].dropna().index]
    
    predictions = model.predict(features)
    
    data_with_predictions = features.copy()
    data_with_predictions['prediction'] = predictions
    
    heatmap = create_heatmap(data_with_predictions, 'prediction')
    
    html_file = 'heatmap.html'
    heatmap.save(html_file)
    
    webbrowser.open('file://' + os.path.realpath(html_file))
