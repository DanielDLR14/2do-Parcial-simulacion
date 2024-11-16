from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error


def entrenamiento(X, y, debug=False):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    trained_model = model.fit(X_train, Y_train)

    if debug:
        Y_pred = trained_model.predict(X_test)
        rmse = root_mean_squared_error(Y_test, Y_pred)
        print(f"RMSE: {rmse}")

    return trained_model
