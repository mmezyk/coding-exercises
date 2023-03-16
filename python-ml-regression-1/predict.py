import json
import os
import pickle

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
INPUT_DATA_FILENAME = 'hidden_test.csv'
FEATURES_TO_SELECT = ["6", "7"]
MODEL_FILENAME = 'gbr_model.pickle'
OUTPUT_DATA_FILENAME = 'gbr_predictions.json'

assert os.path.isfile(os.path.join(ROOT_DIR, INPUT_DATA_FILENAME)), "Input data not found!"
assert os.path.isfile(os.path.join(ROOT_DIR, MODEL_FILENAME)), "Model not found!"

if __name__ == "__main__":
    print('### Data prediction started ###')
    df = pd.read_csv(os.path.join(ROOT_DIR, INPUT_DATA_FILENAME))
    print('# Test data loaded #')
    with open(os.path.join(ROOT_DIR, MODEL_FILENAME), 'rb') as f:
        model = pickle.load(f)
    print('# Model loaded #')
    target_hat = list(model.predict(df[FEATURES_TO_SELECT]))
    with open(os.path.join(ROOT_DIR, OUTPUT_DATA_FILENAME), 'w') as f:
        json.dump(target_hat, f)
    print(f'# Predictions saved. File path: {os.path.join(ROOT_DIR, OUTPUT_DATA_FILENAME)} #')
    print('### Data prediction completed ###')
