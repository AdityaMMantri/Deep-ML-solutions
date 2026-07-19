import numpy as np 
def shuffle_data(X, y, seed=None): 
    rng=np.random.default_rng() 
    combined=list(zip(X,y)) 
    rng.shuffle(combined) 
    X,y=zip(*combined) 
    X=np.asarray(X) 
    y=np.asarray(y) 
    return X,y

import numpy as np

def shuffle_data(X, y, seed=None):
	np.random.seed(seed)
	idx=np.random.permutation(len(X))
	return X[idx], y[idx]