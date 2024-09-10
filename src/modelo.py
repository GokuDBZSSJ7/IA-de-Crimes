from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    X = data[['ano', 'mes', 'id_municipio', 'latrocinio']].dropna()
    
    y = data['homicidio_doloso'].dropna()
    
    X = X.loc[y.index]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model
