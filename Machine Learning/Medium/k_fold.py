import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = list(range(n_samples))

    if shuffle:
        np.random.shuffle(indices)
    base_size=n_samples//k
    extra_samples=n_samples%k
    folds=[]
    start=0

    for i in range(k):
        size=base_size
        if i<extra_samples:
            size+=1
        end=start+size
        folds.append(indices[start:end])
        start=end
    
    result=[]
    for i in range(k):
        test=folds[i]
        train=[]
        for j in range(k):
            if j!=i:
                train.extend(folds[j])
        result.append((train,test))
    return result
