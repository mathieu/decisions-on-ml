#!flask/bin/python
import os
from flask import Flask
from flask import request
import pandas as pd
from sklearn import svm
import pickle

#
#Flask
#

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "Alive!"

@app.route('/prediction/api/v1.0/loan-default', methods=['GET'])
def get_prediction():
    creditScore = float(request.args.get('creditScore'))
    income = float(request.args.get('income'))
    loanAmount = float(request.args.get('loanAmount'))
    monthDuration = float(request.args.get('monthDuration'))
    rate = float(request.args.get('rate'))
    yearlyReimbursement = float(request.args.get('yearlyReimbursement'))

    loaded_model = pickle.load(open('pickle/miniloandefault-svm.pkl', 'rb'))
    prediction = loaded_model.predict([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
    return str(prediction)

@app.route('/test', methods=['GET'])
def get_test():
    feature1 = float(request.args.get('f1'))
    feature2 = float(request.args.get('f2'))
    feature3 = float(request.args.get('f3'))

    loaded_model = pickle.load(open('pickle/miniloandefault-svm.pkl', 'rb'))

    return str("Ok")

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')