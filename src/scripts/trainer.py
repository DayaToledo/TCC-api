from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC

import pickle
import sys

from pre_processor import pre_process
from splitter import split_data
from tester import get_metrics

algorithms_functions = {
    'LogisticRegression': LogisticRegression,
    'KNeighborsClassifier': KNeighborsClassifier,
    'GaussianNB': GaussianNB,
    'DecisionTreeClassifier': DecisionTreeClassifier,
    'AdaBoostClassifier': AdaBoostClassifier,
    'SVC': SVC,
}

algorithm = sys.argv[1]

print()
print(f"Treinando modelo com algoritmo {algorithm}!")

specific = False
algorithm_name = f"{algorithm}"
print(len(sys.argv))
if len(sys.argv) > 2 and sys.argv[2] == "specific":
    specific = True
    algorithm_name = f"{algorithm}_specific"
    print("Treinando de forma especifica, com dados contendo somente 'responsible' ou 'dependable'!")


random_state = 42
X_train, X_test, y_train, y_test = split_data(random_state, pre_process, specific)

model = algorithms_functions[algorithm]()
model.fit(X_train, y_train)

predict = model.predict(X_test)

pickle.dump(model, open(f"src/data/models/model_{algorithm_name}.pkl", 'wb'))
print()
print("Modelo treinado com sucesso e salvo!")

get_metrics(y_test, predict, random_state, algorithm=algorithm_name)
