#!flask/bin/python
import os
from flask import Flask
from flask import request, jsonify
import pandas as pd
from sklearn import svm
from joblib import load

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

json_string = """
{
    "request": {
        "creditScore": "300",
        "income": "100000",
        "loanAmount": "570189",
        "monthDuration": "240",
        "rate": "0.07",
        "yearlyReimbursement": "57195"
    }
}
"""

jsonDictionary = json.loads(json_string)
request = jsonDictionary["request"]
creditScore = float(request["creditScore"])
income = float(request["income"])
loanAmount = float(request["loanAmount"])
monthDuration = float(request["monthDuration"])
rate = float(request["rate"])
yearlyReimbursement = float(request["yearlyReimbursement"])

#query = pd.get_dummies(pd.DataFrame(json_))
#query = query.reindex(columns=model_columns, fill_value=0)

dictionary = load('models/miniloandefault-rfc.joblib')
loaded_model = dictionary['model']
predictionWrapper = loaded_model.predict_proba(
    [[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])

#prediction = list(loaded_model.predict(query))

prediction = predictionWrapper[0]

probabilities = {
  "0": prediction[0],
  "1": prediction[1]
}
responseDictionary = {
  "id": "123",
  "probabilities": probabilities
}

json_string =json.dumps(responseDictionary,indent=4)

print(json_string)

#print(jsonify({'prediction': prediction}))


