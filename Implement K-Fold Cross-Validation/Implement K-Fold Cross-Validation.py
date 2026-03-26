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
    samples = [i for i in range(n_samples)]
    result = []

    if shuffle:
        np.random.shuffle(samples)
    
    fold_size = n_samples // k
    remainder = n_samples % k

    fold_sizes = [fold_size] * k
    for i in range(remainder):
        fold_sizes[i] += 1
    
    for i in range(k):
        test = samples[i * fold_size: i * fold_size + fold_sizes[i]]
        train = []
        for j in samples:
            if j not in test:
                train.append(j)
        result.append((train, test))
    return result
