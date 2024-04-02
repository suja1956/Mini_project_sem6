import pickle4 as pickle
import pickle
import pandas as pd
#from sklearn.preprocessing import StandardScaler

# Loan prediction
# python -m venv venv
# venv\scripts\activate
# pip install -r requirements.txt
# python app.py

# Load the trained model
model = pickle.load(open('PD_credit_risk_model_dev.pkl', 'rb'))

from flask import Flask, render_template, request 
#from utils import preprocessdata 
import flask
app = Flask(__name__) 

@app.route('/') 
def home():
    return render_template('index.html')  
     

@app.route('/predict', methods=['GET', 'POST'])
def predict(): 
    if request.method == 'GET':
        return render_template('predict.html')  



    if request.method == 'POST': 
        # Extract data from form
        print("starrt")
        NumberOfDependents = int(request.form['NumberOfDependents'])
        RevolvingUtilizationOfUnsecuredLines = float(request.form['RevolvingUtilizationOfUnsecuredLines'])
        age = int(request.form['age'])
        NumberOfTime30_59DaysPastDueNotWorse = int(request.form['NumberOfTime30-59DaysPastDueNotWorse'])
        DebtRatio = float(request.form['DebtRatio'])
        MonthlyIncome = float(request.form['MonthlyIncome'])
        NumberOfOpenCreditLinesAndLoans = int(request.form['NumberOfOpenCreditLinesAndLoans'])
        NumberOfTimes90DaysLate = int(request.form['NumberOfTimes90DaysLate'])
        NumberRealEstateLoansOrLines = int(request.form['NumberRealEstateLoansOrLines'])
        NumberOfTime60_89DaysPastDueNotWorse = int(request.form['NumberOfTime60-89DaysPastDueNotWorse'])

        # Create DataFrame with correct feature names
        input_data = pd.DataFrame({
            'RevolvingUtilizationOfUnsecuredLines': [RevolvingUtilizationOfUnsecuredLines],
            'age': [age],
            'NumberOfTime30-59DaysPastDueNotWorse': [NumberOfTime30_59DaysPastDueNotWorse],  # Corrected feature name
            'DebtRatio': [DebtRatio],
            'MonthlyIncome': [MonthlyIncome],
            'NumberOfOpenCreditLinesAndLoans': [NumberOfOpenCreditLinesAndLoans],
            'NumberOfTimes90DaysLate': [NumberOfTimes90DaysLate],
            'NumberRealEstateLoansOrLines': [NumberRealEstateLoansOrLines],
            'NumberOfTime60-89DaysPastDueNotWorse': [NumberOfTime60_89DaysPastDueNotWorse],
            'NumberOfDependents': [NumberOfDependents]  # Corrected feature name
        })

        # Make prediction
        print("model me chala")
        prediction = model.predict(input_data)
        print(prediction[0])

        return render_template('predict.html', prediction=prediction) 
 

# @app.route('/indi', methods=['GET', 'POST'])
# def calc():
#     if request.method == 'GET':
#         return render_template('individual.html')

if __name__ == '__main__': 
    app.run(debug=True) 