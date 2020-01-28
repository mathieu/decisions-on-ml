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

@app.route('/prediction/api/v1.0/loandefault', methods=['GET'])
def get_loandefault():
    creditScore = float(request.args.get('creditScore'))
    income = float(request.args.get('income'))
    loanAmount = float(request.args.get('loanAmount'))
    monthDuration = float(request.args.get('monthDuration'))
    rate = float(request.args.get('rate'))
    yearlyReimbursement = float(request.args.get('yearlyReimbursement'))

    loaded_model = pickle.load(open('pickle/miniloandefault-svm.pkl', 'rb'))
    prediction = loaded_model.predict([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
    return str(prediction)

@app.route('/automation/api/v1.0/prediction', methods=['GET'])
def get_prediction():
    model = request.args.get('model')
    version = request.args.get('version')
    creditScore = float(request.args.get('creditScore'))
    income = float(request.args.get('income'))
    loanAmount = float(request.args.get('loanAmount'))
    monthDuration = float(request.args.get('monthDuration'))
    rate = float(request.args.get('rate'))
    yearlyReimbursement = float(request.args.get('yearlyReimbursement'))

    loaded_model = pickle.load(open('pickle/miniloandefault-svm.pkl', 'rb'))
    prediction = loaded_model.predict([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
    return str(prediction)

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')
