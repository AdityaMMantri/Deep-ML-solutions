import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float],float):
	X=np.array(features)
	W=np.array(weights)
	y=np.array(labels)

	z=X @ W + bias
	y_hat=1/(1+np.exp(-z))

	mse=np.mean((y_hat - y) ** 2)
	y_hat=np.round(y_hat, 4).tolist()
	mse=round(float(mse), 4)

	return y_hat, mse