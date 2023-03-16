# Regression on the tabular data.

You have a dataset (train.csv) that contains 53 anonymized features and a target
column. Your task is to build a model that predicts a target based on the proposed
features. Provide predictions for the hidden_test.csv file. Target metric is RMSE.

### Applied algorithm: 

Gradient Boosting Regressor (GBR) with hyperparameter fine-tuning

### Files:

main.ipynb - jupyter notebook with exploratory data analysis

train.py - python script for model training

predict.py - python script for model inference on test data

gbr_params.json - tuned hyperparameter set for GBR

### Info:

1. Run train.py - it will create and save a model as gbr_model.pickle in a working directory.
2. Run predict.py - it will load a generated model and apply it to hidden_test.csv data.
