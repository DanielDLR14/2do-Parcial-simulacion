from entrenamiento_modelo import entrenamiento
from procesamiento_data import cargar_data
import questionary
import pandas as pd

# Ruta al dataset de escasez de agua
dataset = "C:/Users/desktop/Desktop/2do Parcial - Simulacion de Sistemas/Ejercicio 1/data/escasez_agua_dataset.csv"

def predict():
    X, y, dict_of_cast = cargar_data(dataset)
    model = entrenamiento(X, y, debug=False)

    result = {}

    # Preguntar por las columnas categóricas en `dict_of_cast`
    for key in dict_of_cast:
        choices = []
        
        for i in range(len(dict_of_cast[key]["before"])):
            choices.append(
                {
                    "name": f"{dict_of_cast[key]['before'][i]}",
                    "value": dict_of_cast[key]["after"][i],
                }
            )

        choice = questionary.select(
            f"Choose an option for {key}:", choices=choices
        ).ask()
        result[key] = choice

    # Convertir `result` a DataFrame para la predicción
    input_data = pd.DataFrame(result, index=[0])
    input_data = input_data[
        [
            "crecimiento_poblacional",
            "consumo_medio_anual",
            "tasa_decrecimiento_reservas",
            "precipitaciones_anuales",
            "temperatura_promedio"
        ]
    ]

    # Hacer la predicción
    prediction = model.predict(input_data)
    print(f"Predicción del año de escasez de agua: {prediction}")

# Llamar a la función para realizar la predicción
predict()