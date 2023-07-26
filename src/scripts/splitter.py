import numpy as np
import os

from sklearn.model_selection import train_test_split

np_array_path = os.path.abspath("src/data/np_arrays/")

def split_data(random_state, pre_process, specific=False):
    if specific:
        np_array_X = f"{np_array_path}/X_specific.npy"
        np_array_y = f"{np_array_path}/y_specific.npy"
    else: 
        np_array_X = f"{np_array_path}/X.npy"
        np_array_y = f"{np_array_path}/y.npy"

    if not (
        os.path.exists(np_array_X)
        and os.path.exists(np_array_y)
    ):
        X, y = pre_process(specific)
        X = np.array(X)
        y = np.array(y)
        np.save(np_array_X, X)
        np.save(np_array_y, y)

    X = np.load(np_array_X, allow_pickle=True)
    y = np.load(np_array_y, allow_pickle=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    return X_train, X_test, y_train, y_test
