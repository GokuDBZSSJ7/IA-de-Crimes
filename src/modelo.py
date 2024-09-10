import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def treinar_modelo(X_train, y_train):
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)
    return modelo

def avaliar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    return acuracia

def salvar_modelo(modelo, caminho_arquivo):
    with open(caminho_arquivo, 'wb') as f:
        pickle.dump(modelo, f)

def carregar_modelo(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as f:
        modelo = pickle.load(f)
    return modelo
