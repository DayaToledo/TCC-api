from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC

import pickle
import sys

from pre_processor import pre_process
from split_dataset import get_data
from metrics import get_metrics

algorithms_functions = {
    'LogisticRegression': LogisticRegression,
    'KNeighborsClassifier': KNeighborsClassifier,
    'GaussianNB': GaussianNB,
    'DecisionTreeClassifier': DecisionTreeClassifier,
    'AdaBoostClassifier': AdaBoostClassifier,
    'SVC': SVC
}

algorithm = sys.argv[1]
print()
print(f"Train model with {algorithm} algorithm!")

random_state = 42
X_train, X_test, y_train, y_test = get_data(random_state, pre_process)

model = algorithms_functions[algorithm]()
model.fit(X_train, y_train)

predict = model.predict(X_test)

pickle.dump(model, open(f"src/data/models/model_{algorithm}.pkl", 'wb'))
print()
print("Model successfully trained and saved!")

get_metrics(y_test, predict, random_state, algorithm)
