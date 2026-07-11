import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	X=np.array(features)
	W=np.array(weights)
	y=np.array(labels)

	z=X @ W + bias
	probabilities=1/(1+np.exp(-z))

	mse=np.mean((probabilities - y) ** 2)
	probabilities=np.round(probabilities, 4).tolist()
	mse=round(float(mse), 4)

	return probabilities, mse