import os
import pandas as pd
import pickle

def main():
    try:
        samples_path = os.path.abspath("src/data/samples/")
        test_data = pd.read_csv(f"{samples_path}/dataset1.csv", sep=',')
        test_data = test_data.sample()
        print(test_data)
        personality_traits = ["EXT", "AGR", "CSN", "EST", "OPN"]
        test_data = test_data[personality_result]
        print(test_data)
        model = pickle.load(open('src/data/models/model.pkl', 'rb'))
        prediction = model.predict(test_data)[0]
        print(prediction)
        return prediction
    except Exception as error:
        print("Um erro ocorreu.", error)
        return api_response({"Erro": error}, 500)

main()