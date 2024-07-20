# Election prediction webapp
This webapp predicts party support in Swiss elections based on demographic data using a machine learning model.

## Features
- Predictions of party support probabilities based on demographics
- Visualization of prediction results


## Installation
1. Clone the repository: 
```bash
git clone https://github.com/lauramauricio/election-prediction-webapp.git
cd election-prediction-webapp
```

2. Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the required packages:
``` 
pip install -r requirements.txt
```

## Run the app

**To only run the web application**, use `notebooks/3-app_gb.ipynb`. Execute all the cells. 
You will be able to use the app in the last cell.

If you have an issue like `Address port already in use`, change the port number, to `8001` for example. The app should now be accessible at `http://localhost:8000` (or any other port).


## Model training and hyperparameter tuning

**To reproduce the whole pipeline** (data preprocessing, hyperparameter tuning and final model training), run the other jupyter notebooks in order, which are located in the `notebooks` directory.


## Model
This app uses a Gradient Boosting Classifier trained on Selects survey data from 1971 to 2019. The model takes into account various demographic factors to predict party support probabilities.


## Data
The model is trained on data from the Swiss Election Study (Selects)". The data includes demographic information such as age, gender, education level, income, and more.

