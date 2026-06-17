import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    y = y.reshape(-1, 1) 	
    theta = np.zeros((n, 1))
    for i in range (iterations):
        y_hat=X @ theta
        error=y_hat-y
        gradient=(1/m)*(X.T @ error)
        theta-=alpha*gradient
        
    return np.round(theta.flatten(), 4) 	# Rounded to 4 decimals
X = np.array([[1, 1],
              [1, 2],
              [1, 3]])

y = np.array([1, 2, 3])

alpha = 0.01
iterations = 100
print(linear_regression_gradient_descent(X, y, alpha, iterations))