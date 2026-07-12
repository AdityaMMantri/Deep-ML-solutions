import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	
    X=np.array(features)
    y=np.array(labels)
    W=np.array(initial_weights, dtype=float)
    b=float(initial_bias)

    mse_values = []

    for _ in range(epochs):
        z=X @ W+b
        y_hat=1/(1 + np.exp(-z))

        mse = np.mean((y_hat - y) ** 2)
        mse_values.append(round(float(mse), 4))

        dL_dy_hat = (2 * (y_hat-y))/len(y)
        dy_hat_dz = y_hat*(1-y_hat)
        dL_dz = dL_dy_hat * dy_hat_dz

        dW = X.T @ dL_dz
        db = np.sum(dL_dz)

        W = W - learning_rate * dW
        b = b - learning_rate * db

    updated_weights = np.round(W, 4)
    updated_bias = round(float(b), 4)

    return updated_weights, updated_bias, mse_values	