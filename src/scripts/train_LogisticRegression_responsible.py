from sklearn.linear_model import LogisticRegression
import pickle

from pre_processor import pre_process_responsible
from split_dataset import get_data
from metrics import get_metrics

print()
print(f"Train model with LogisticRegression algorithm and data responsible or dependable!")

random_state = 42
X_train, X_test, y_train, y_test = get_data(random_state, pre_process_responsible)

model = LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
model.fit(X_train, y_train)

predict = model.predict(X_test)

pickle.dump(model, open("src/data/models/model_LogisticRegression_responsible.pkl", 'wb'))
print()
print("Model successfully trained and saved!")

get_metrics(y_test, predict, random_state, algorithm="LogisticRegression_responsible")
