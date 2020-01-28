#
# This program builds a SVM model to predict a loan payment default.
# It reads a labelled dataset of loan payments, makes the model, measures its accuracy and performs unit tests.
# It ends by a serialization through pickle. The serialized model is then used by the main program that serves it.
#

import os
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
prediction = SVM.predict([[397,160982,570189,240,0.07,57195]]) # expected 1 meaning default
print("prediction with SVM: " + str(prediction) + " expect [1]")
decision_function = SVM.decision_function([[397,160982,570189,240,0.07,57195]]) # expected 1
print("Confidence levels:", decision_function)

prediction = SVM.predict([[580,66037,168781,120,0.09,16187]]) # expected 0
print("prediction with SVM: " + str(prediction) + " expect [0]")
decision_function = SVM.decision_function([[580,66037,168781,120,0.09,16187]]) # expected 0 meaning absence of default
print("Confidence levels:", decision_function)

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