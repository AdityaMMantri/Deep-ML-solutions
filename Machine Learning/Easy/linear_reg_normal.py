import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)


    # normal equation using pseudo-inverse for numerical stability
    theta = np.linalg.pinv(X.T @ X) @ X.T @ y

    # round to 4 decimal places
    theta = np.round(theta, 4)
    return theta
print(linear_regression_normal_equation(X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]))