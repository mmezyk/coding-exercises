import json
import os
import pickle

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
INPUT_DATA_FILENAME = 'train.csv'
FEATURES_TO_SELECT = ["6", "7"]
PARAMS_FILENAME = 'gbr_params.json'
MODEL_FILENAME = 'gbr_model.pickle'

assert os.path.isfile(os.path.join(ROOT_DIR, INPUT_DATA_FILENAME)), "Input data not found!"
assert os.path.isfile(os.path.join(ROOT_DIR, PARAMS_FILENAME)), "Params data not found!"

if __name__ == "__main__":
    print('### Model creation started ###')
    df = pd.read_csv(os.path.join(ROOT_DIR, INPUT_DATA_FILENAME))
    print('# Train data loaded #')
    with open(os.path.join(ROOT_DIR, PARAMS_FILENAME), 'r') as f:
        gbr_params = json.load(f)
    print('# Tuned hyperparameter set loaded #')
    gbr = GradientBoostingRegressor(**gbr_params)
    gbr.fit(df.loc[:, FEATURES_TO_SELECT], df.target)
    print('# Model trained #')
    with open(os.path.join(ROOT_DIR, MODEL_FILENAME), 'wb') as f:
        pickle.dump(gbr, f)
    print(f'# Model saved. File path: {os.path.join(ROOT_DIR, MODEL_FILENAME)}. #')
    print('### Model creation completed ###')
