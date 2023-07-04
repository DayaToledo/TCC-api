import numpy as np
import os

from sklearn.model_selection import train_test_split

np_array_path = os.path.abspath("src/data/np_arrays/")

def get_data(random_state, pre_process):
    if not (
        os.path.exists(f"{np_array_path}/X.npy")
        and os.path.exists(f"{np_array_path}/y.npy")
    ):
        X, y = pre_process()
        X = np.array(X)
        y = np.array(y)
        np.save(f"src/data/np_arrays/X.npy", X)
        np.save(f"src/data/np_arrays/y.npy", y)

    X = np.load(f"src/data/np_arrays/X.npy", allow_pickle=True)
    y = np.load(f"src/data/np_arrays/y.npy", allow_pickle=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    return X_train, X_test, y_train, y_test
