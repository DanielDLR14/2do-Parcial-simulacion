import pandas as pd
from sklearn.preprocessing import LabelEncoder

def cargar_data(csv_path):
    df = pd.read_csv(csv_path)

    df = df[(df["densidad_poblacional"] >= 50) & (df["densidad_poblacional"] <= 500)]

    label_encoder = LabelEncoder()
    list_of_columns = [
        "zona_riesgo",
        "tipo_evento_climatico",
        "región",
        "nivel_educativo",
        "ocupación",
        "estado_familiar"
    ]

    dict_of_cast = {}
    for column in list_of_columns:
        dict_of_cast[column] = {}
        dict_of_cast[column]["before"] = df[column].unique()  
        df[column] = label_encoder.fit_transform(df[column]) 
        dict_of_cast[column]["after"] = df[column].unique()   
    X = df.drop("migración_estimada", axis=1)  
    y = df["migración_estimada"]                

    return X, y, dict_of_cast
