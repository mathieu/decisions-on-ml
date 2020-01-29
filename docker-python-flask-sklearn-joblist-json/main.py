#!flask/bin/python
import os
from flask import Flask, jsonify
from flask import request, jsonify
import pandas as pd
from joblib import load

import json
import requests
#
#Flask
#

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "Ok"

@app.route('/automation/api/v1.0/prediction', methods=['POST'])
def get_pred():
    try:
        jsonDictionary = request.json
        print(jsonDictionary)
        jsonPayloadDictionary = jsonDictionary["request"]

        creditScore = float(jsonPayloadDictionary["creditScore"])
        income = float(jsonPayloadDictionary["income"])
        loanAmount = float(jsonPayloadDictionary["loanAmount"])
        monthDuration = float(jsonPayloadDictionary["monthDuration"])
        rate = float(jsonPayloadDictionary["rate"])
        yearlyReimbursement = float(jsonPayloadDictionary["yearlyReimbursement"])

        dictionary = load('models/miniloandefault-rfc.joblib')
        loaded_model = dictionary['model']
        predictionWrapper = loaded_model.predict_proba(
            [[creditScore, income, loanAmount, monthDuration, rate, yearlyReimbursement]])

        prediction = predictionWrapper[0]

        probabilities = {
            "0": prediction[0],
            "1": prediction[1]
        }
        responseDictionary = {
            "id": "123",
            "probabilities": probabilities
        }

        json_string = json.dumps(responseDictionary, indent=4)

        print(json_string)

        return json_string

        #return jsonify({'prediction': prediction})

    except:
        return "KO"
        #return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    #if os.environ['ENVIRONMENT'] == 'production':
    #    app.run(port=80,host='0.0.0.0')
    #if os.environ['ENVIRONMENT'] == 'local':
    app.run(port=5000,host='0.0.0.0')
