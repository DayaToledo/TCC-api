
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, f1_score, max_error

def get_metrics(y_test, predict, random_state, algorithm):
    precision = format(precision_score(y_test, predict, average='macro', zero_division=0) * 100, '.2f')
    f1 = format(f1_score(y_test, predict, average='macro') * 100, '.2f')
    accuracy = format(accuracy_score(y_test, predict) * 100, '.2f')

    print()
    print(f"Temos as seguintes métricas com um random_state de {random_state}")
    print (f"Acurácia: {accuracy}%")
    print (f"Precisão: {precision}%")
    print (f"F1: {f1}%")
    print()

    columns = ['Algoritmo','Acurácia','Precisão', 'F1']
    csv_name_path = "src/data/metrics.csv"
    if not (os.path.exists(csv_name_path)):
        # rows = {}
        df = pd.DataFrame(data=None, index=[0], columns=columns)
        df.to_csv(csv_name_path, sep=',', mode = 'a', header = True)

    data = {
        'Algoritmo': [algorithm], 
        'Acurácia': [accuracy],
        'Precisão': [precision],
        'F1': [f1]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_name_path, sep=',', mode = 'a', header = False)
    return
