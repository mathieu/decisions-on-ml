#!flask/bin/python
import os
from flask import Flask
from flask import request
import pandas as pd
from sklearn import svm
import pickle

data = pd.read_csv('data/miniloan-decisions-default-1K.csv', sep=',',header=0)
data.head()
print("Number of records: " + str(data.count()))

from sklearn.model_selection import train_test_split
from sklearn import metrics

#creditScore,income,loanAmount,monthDuration,rate,yearlyReimbursement,paymentDefault
X=data[['creditScore', 'income', 'loanAmount', 'monthDuration', 'rate' , 'yearlyReimbursement' ]] # Features
y=data['paymentDefault']  # Label

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

SVM = svm.LinearSVC()
SVM.fit(X_train, y_train)

# Model Accuracy, how often is the classifier correct?
y_pred=SVM.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Unit test
prediction = SVM.predict([[397,160982,570189,240,0.07,57195]]) # expected 1
print("prediction with SVM: " + str(prediction) + " expect [1]")
prediction = SVM.predict([[580,66037,168781,120,0.09,16187]]) # expected 0
print("prediction with SVM: " + str(prediction) + " expect [0]")

creditScore = 397
income = 160982
loanAmount = 570189
monthDuration = 240
rate = 0.07
yearlyReimbursement = 57195
prediction = SVM.predict([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
print("prediction with SVM: " + str(prediction) + " expect [1]")

#Model serialization
pickle.dump(SVM, open('pickle/miniloandefault-svm.pkl', 'wb'))

#Testing deserialized model
loaded_model = pickle.load(open('pickle/miniloandefault-svm.pkl', 'rb'))
prediction = loaded_model.predict([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
print("prediction with serialized SVM: " + str(prediction) + " expect [1]")

#
#Flask
#

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/prediction/api/v1.0/some_prediction', methods=['GET'])
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

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')