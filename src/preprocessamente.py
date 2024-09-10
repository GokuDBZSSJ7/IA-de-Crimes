import pandas as pd

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    return data
