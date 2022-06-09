# import gc
import os
import pandas as pd
import tensorflow as tf
from pre_processor import get_x

def main():
    try:
        # test_data = event["data"]

        samples_path = os.path.abspath("src/data/samples/")
        test_data = pd.read_csv(f"{samples_path}/test.csv", sep='\t')

        test_data = get_x(test_data)

        model = tf.keras.models.load_model("src/data/models/model.h5")
        predictions = model.predict(test_data)
        # garbage_collect(model)
        
        parsed_prediction = parse_prediction(predictions)

        print(parsed_prediction)

        return api_response(parsed_prediction, 200)
    except Exception as error:
        print("An error ocurred.", error)
        return api_response({"error": error}, 500)

# def garbage_collect(model):
#     del model
#     gc.collect()
#     tf.keras.backend.clear_session()


def parse_prediction(predictions):
    return {
        "EXT_PER": predictions[0][0][0],
        "AGR_PER": predictions[1][0][0],
        "CSN_PER": predictions[2][0][0],
        "EST_PER": predictions[3][0][0],
        "OPN_PER": predictions[4][0][0]
    }


def api_response(body, status_code):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": body,
    }

main()