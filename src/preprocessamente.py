import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def carregar_dados(caminho_arquivo):
    if caminho_arquivo.endswith('.csv'):
        df = pd.read_csv(caminho_arquivo)
    else:
        df = pd.read_excel(caminho_arquivo)
    return df

def preprocessar_dados(df):
    print("Colunas disponíveis:", df.columns)
    
    coluna_alvo = 'homicidio_doloso'
    
    if coluna_alvo not in df.columns:
        raise ValueError(f"A coluna '{coluna_alvo}' não foi encontrada no DataFrame.")
    
    df = df.dropna()
    
    colunas_nao_numericas = df.select_dtypes(include=['object']).columns
    print("Colunas não numéricas:", colunas_nao_numericas)
    
    le = LabelEncoder()
    for coluna in colunas_nao_numericas:
        df.loc[:, coluna] = le.fit_transform(df[coluna].astype(str))
    
    X = df.drop(coluna_alvo, axis=1)
    y = df[coluna_alvo]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
