from preprocessamente import carregar_dados, preprocessar_dados
from modelo import treinar_modelo, avaliar_modelo, salvar_modelo, carregar_modelo

def main():
    df = carregar_dados('../dados/dados.csv')
    X_train, X_test, y_train, y_test = preprocessar_dados(df)

    modelo = treinar_modelo(X_train, y_train)

    acuracia = avaliar_modelo(modelo, X_test, y_test)
    print(f'Acurácia do modelo: {acuracia}')

    salvar_modelo(modelo, '../models/modelo.pkl')

    modelo_carregado = carregar_modelo('../models/modelo.pkl')
    

if __name__ == '__main__':
    main()
