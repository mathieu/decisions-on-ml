#
# This program builds a SVM model to predict a loan payment default.
# It reads a labelled dataset of loan payments, makes the model, measures its accuracy and performs unit tests.
# It ends by a serialization through models. The serialized model is then used by the main program that serves it.
#

import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
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
# 70% training and 30% test
# deterministic split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) # 70% training and 30% test

model = RandomForestClassifier(max_depth=2, random_state=0).fit(X_train, y_train)
print(model.feature_importances_)


# Model Accuracy, how often is the classifier correct?
y_pred=model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)

#Unit test
prediction = model.predict_proba([[397,160982,570189,240,0.07,57195]]) # expected 1 meaning default
print("prediction with Random Forest Classifier: " + str(prediction) + " expect [1]")

prediction = model.predict_proba([[580,66037,168781,120,0.09,16187]]) # expected 0
print("prediction with Random Forest Classifier: " + str(prediction) + " expect [0]")


#Test cut values for samples
prediction = model.predict_proba([[400,17500,27500,12,0.05,40000]]) # expected 0
print("prediction test 1 with Random Forest Classifier: " + str(prediction) + " expect [0]")

prediction = model.predict_proba([[600,80000,400000,120,0.05,75195]]) # expected 0
print("prediction test 2 with Random Forest Classifier: " + str(prediction) + " expect [0]")

prediction = model.predict_proba([[600,80000,1000000,120,0.05,75195]]) # expected 0
print("prediction test 3 with Random Forest Classifier: " + str(prediction) + " expect [0]")



creditScore = 397
income = 160982
loanAmount = 570189
monthDuration = 240
rate = 0.07
yearlyReimbursement = 57195

prediction = model.predict_proba([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
print("prediction with Random Forest Classifier: " + str(prediction) + " expect [1]")

#Model serialization

toBePersisted = dict({
    'model': model,
    'metadata': {
        'name': 'loan payment default classification',
        'author': 'Pierre Feillet',
        'date': '2020-01-28T15:45:00CEST',
        'metrics': {
            'accuracy': accuracy
        }
    }
})

from joblib import dump
dump(toBePersisted, 'models/miniloandefault-rfc.joblib')

#Testing deserialized model

from joblib import load
dictionary = load('models/miniloandefault-rfc.joblib')
loaded_model = dictionary['model']
prediction = loaded_model.predict_proba([[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])
print("prediction with serialized Random Forest Classifier: " + str(prediction) + " expect [1]")