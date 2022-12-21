# import gc
import os
import pandas as pd
import pickle

def main():
    try:
        samples_path = os.path.abspath("src/data/samples/")
        test_data = pd.read_csv(f"{samples_path}/test.csv", sep=',')
        print(test_data)
        model = pickle.load(open('src/data/models/model.pkl', 'rb'))
        prediction = model.predict(test_data)[0]
        print(prediction)
        return prediction
    except Exception as error:
        print("An error ocurred.", error)
        return api_response({"error": error}, 500)

main()