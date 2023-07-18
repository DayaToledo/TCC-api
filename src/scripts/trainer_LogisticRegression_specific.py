from sklearn.linear_model import LogisticRegression
import pickle

from pre_processor import pre_process_specific
from splitter import split_data
from tester import get_metrics

print()
print(f"Treinando modelo com algoritmo LogisticRegression e com dados contendo somente 'responsible' ou 'dependable'!")

random_state = 42
X_train, X_test, y_train, y_test = split_data(random_state, pre_process_specific, algorithm='specific')

model = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
model.fit(X_train, y_train)

predict = model.predict(X_test)

pickle.dump(model, open("src/data/models/model_LogisticRegression_specific.pkl", 'wb'))
print()
print("Modelo treinado com sucesso e salvo!")

get_metrics(y_test, predict, random_state, algorithm="LogisticRegression_specific")
