from preprocessamente import load_and_preprocess_data
from modelo import train_model
from visualize import create_heatmap
import webbrowser
import os

if __name__ == "__main__":
    # Carregar e pré-processar os dados
    data = load_and_preprocess_data('../dados/crimes.csv')
    
    # Treinar o modelo
    model = train_model(data)
    
    # Usar as mesmas colunas para as previsões
    features = data[['ano', 'mes', 'id_municipio', 'latrocinio']].dropna()
    
    # Garantir que os índices estejam consistentes
    features = features.loc[data['homicidio_doloso'].dropna().index]
    
    # Fazer previsões
    predictions = model.predict(features)
    
    # Criar um DataFrame temporário com as previsões
    data_with_predictions = features.copy()
    data_with_predictions['prediction'] = predictions
    
    # Criar o heatmap
    heatmap = create_heatmap(data_with_predictions, 'prediction')
    
    # Salvar o heatmap como um arquivo HTML
    html_file = 'heatmap.html'
    heatmap.save(html_file)
    
    # Abrir o HTML no navegador
    webbrowser.open('file://' + os.path.realpath(html_file))
