import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    n=len(X)//2
    subsets=[]
    if replacements==True:
        for i in range(n_subsets):
            idx = np.random.choice(len(X) ,size=len(X),replace=True)
            subsets.append((X[idx].tolist(), y[idx].tolist()))   
    else:
        for i in range(n_subsets):
            idx = np.random.choice(len(X) ,size=n,replace=False)
            subsets.append((X[idx].tolist(), y[idx].tolist()))
    return subsets
        

    