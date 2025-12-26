## utils to use for all algos
import numpy as np

def train_test_split(data,split_ratio):
    np.random.shuffle(data)
    split_index=int(split_ratio*len(data))

    train_data=data[:split_index]
    test_data=data[split_index:]
    return train_data,test_data

def train_test_split_xy(x,y,test_size, shuffle=True,random_state=None):
    assert len(x)==len(y),"x and y must be same length"
    
    if random_state is not None:
        np.random.seed(random_state)
    indices=np.arange(len(x))
    if shuffle:
        np.random.shuffle(indices)
    split_index=int(1-test_size)*len(x)
    train_idx = indices[:split_index]
    test_idx = indices[split_index:]

    X_train = x[train_idx]
    X_test = x[test_idx]
    y_train = y[train_idx]
    y_test = y[test_idx]

    return X_train, X_test, y_train, y_test
