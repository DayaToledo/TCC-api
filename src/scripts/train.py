import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

from pre_processor import pre_process

np_array_path = os.path.abspath("src/data/np_arrays/")

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 1)

model = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=100)
model.fit(X_train, y_train)

predict = model.predict(X_test)
accuracy = accuracy_score(y_test, predict) * 100
print ("The accuracy was {:.2f}%.".format(accuracy))

pickle.dump(model, open("src/data/models/model.pkl", 'wb'))
print("Model sucessfully trained and saved!")
