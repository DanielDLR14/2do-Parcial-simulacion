from entrenamiento_modelo import entrenamiento
from procesamiento_data import cargar_data
import questionary
import pandas as pd

dataset = "C:/Users/desktop/Desktop/2do Parcial - Simulacion de Sistemas/Ejercicio 13/data/migracion_climatica (2).csv"

def predict():
    x, y, dict_of_cast = cargar_data(dataset)
    model = entrenamiento(x, y, debug=False)

    result = {}

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

    result["eventos_climáticos_extremos"] = int(questionary.text(
        "Ingrese el número de eventos climáticos extremos (0-20):",
        validate=lambda text: text.isdigit() and 0 <= int(text) <= 20
    ).ask())

    result["deterioro_ambiente"] = float(questionary.text(
        "Ingrese el índice de deterioro ambiental (0-100):",
        validate=lambda text: text.replace('.', '', 1).isdigit() and 0 <= float(text) <= 100
    ).ask())

    result["oportunidades_económicas"] = float(questionary.text(
        "Ingrese el índice de oportunidades económicas (0-100):",
        validate=lambda text: text.replace('.', '', 1).isdigit() and 0 <= float(text) <= 100
    ).ask())

    result["densidad_poblacional"] = int(questionary.text(
        "Ingrese la densidad poblacional (50-500 personas/km²):",
        validate=lambda text: text.isdigit() and 50 <= int(text) <= 500
    ).ask())

    input_data = pd.DataFrame(result, index=[0])
    input_data = input_data[
        [
            "eventos_climáticos_extremos",
            "deterioro_ambiente",
            "oportunidades_económicas",
            "densidad_poblacional",
            "zona_riesgo",
            "tipo_evento_climatico",
            "región",
            "nivel_educativo",
            "ocupación",
            "estado_familiar"
        ]
    ]

    prediction = model.predict(input_data)
    print(f"Prediction: {prediction}")

predict()