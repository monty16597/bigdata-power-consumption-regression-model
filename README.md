# Power Consumption using Regression Model

## Introduction
Project aim to predict power consumption of the Tetuan city using XGBRegression Model.

## Data
Data is collected from the [Kaggle](https://www.kaggle.com/uciml/electric-power-consumption-data-set) and it contains the power consumption of the Tetuan city from 2006 to 2010.

## Model
XGBRegression Model is used to predict the power consumption of the Tetuan city.

## Codebase

### gluecode.py
This file contains the code to load the data, preprocess the data, train the model and save the model. It adds features like `year`, `month`, `day`, `hour`, `minute` and `second` to the data.

### power Consumption Prediction.ipynb
This file contains the code to load the model and predict the power consumption of the Tetuan city. It also exports the model to the `webapp` folder. Webapp uses this model to predict the power consumption of the Tetuan city.

### webapp
This folder contains the code to create a webapp using Flask. The webapp takes the input from the user and predicts the power consumption of the Tetuan city.

## Conclusion
The model is able to predict the power consumption of the Tetuan city with 95% accuracy.
