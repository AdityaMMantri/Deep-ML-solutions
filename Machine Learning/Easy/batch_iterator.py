import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    res=[]
    for i in range(0,len(y),batch_size):
        if y is not None:
            res.append([X[i:i+batch_size].tolist(),y[i:i+batch_size].tolist()])
        else:
            res.append(X[i:i+batch_size].tolist())
    return res
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))