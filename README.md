# Loan Default Prediction App

This project is a Loan Default Prediction application that aims to help financial institutions assess the risk of loan defaults using machine learning techniques. The app predicts whether a borrower is likely to default on a loan based on various features.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Machine Learning Model](#machine-learning-model)

## Features

- Predict loan default likelihood based on input features.
- User-friendly interface for inputting borrower data.
- Visualizations to help understand the prediction results.
- Easy to extend and customize for other prediction models.

## Technologies Used

- **Python**: Backend language for the application.
- **Flask**: Web framework for building and serving the app.
- **Pandas**: Data manipulation library.
- **Scikit-learn**: Machine learning library.
- **Matplotlib & Seaborn**: Data visualization tools.
- **HTML/CSS**: Frontend design for a user-friendly interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/suja1956/Mini_project_sem6.git
   cd Mini_project_sem6

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3.pip install -r requirements.txt

## Usage

1.Start the Flask server:
  ```bash
  python app.py
```
2.Open your web browser and go to http://127.0.0.1:5000.

## Data

The dataset used in this project contains various features related to loan applicants, such as:

   Loan amount
   Interest rate
   Borrower's income
   Credit score
   Employment status, etc.

## Machine learning model

   The app uses a Random Forest classifier from Scikit-learn for loan default prediction. The model is trained on labeled data and predicts the likelihood of a borrower defaulting based    on the features provided.


   
