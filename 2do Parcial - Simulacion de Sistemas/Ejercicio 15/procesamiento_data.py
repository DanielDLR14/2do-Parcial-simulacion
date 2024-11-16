import pandas as pd
from sklearn.preprocessing import LabelEncoder

def cargar_data(csv_path):
    # Cargar el dataset
    df = pd.read_csv(csv_path)

    # Codificación de las columnas categóricas a valores numéricos
    label_encoder = LabelEncoder()
    list_of_columns = [
        "expansión_agroindustria",
        "políticas_forestales",
        "áreas_protegidas",
        "presión_demanda_alimentos"
    ]

    dict_of_cast = {}
    for column in list_of_columns:
        dict_of_cast[column] = {}
        dict_of_cast[column]["before"] = df[column].unique()  # Valores originales
        df[column] = label_encoder.fit_transform(df[column])  # Transformar a enteros
        dict_of_cast[column]["after"] = df[column].unique()   # Valores transformados

    # Definir variables independientes y dependiente
    X = df.drop("pérdida_bosque", axis=1)  # Variables independientes
    y = df["pérdida_bosque"]               # Variable dependiente

    return X, y, dict_of_cast