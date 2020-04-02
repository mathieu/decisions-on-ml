#!flask/bin/python
import os
import uuid
from flask import Flask, jsonify
from flask import request, jsonify
from flask_restplus import Api, Resource, fields
from flask_restplus import reqparse

import pandas as pd
from joblib import load
import pickle

import json
import requests

#
# Model registering
#

modelDictionary = dict({
    'models': [
        {
            'path': "models/miniloandefault-rfc.joblib",
        },
        {
            'path': "models/miniloandefault-svm.joblib",
        },
        {
            'path': "models/iris-svc.joblib",
        }
    ]
})

# todo
# Propagate the joblib metadata into the model management dictionary

#
# Flask
#

app = Flask(__name__)
api = Api(app)

ns = api.namespace('automation/api/v1.0/prediction/admin', description='administration')


@ns.route('/isAlive')  # Create a URL route to this resource
class HeartBeat(Resource):  # Create a RESTful resource
    def get(self):  # Create GET endpoint
        return {'answer': 'ok'}


@ns.route("/models")
class Model(Resource):
    def get(self):
        """Returns the list of ML models."""
        return modelDictionary


model_key_descriptor = api.model('ModelKeyDescriptor', {
    'name': fields.String(required=True, description="Name of the model", help="Name cannot be blank."),
    'version': fields.String(required=True, description="Version of the model", help="Name cannot be blank."),
    'format': fields.String(required=True, description="Format of the model", help="Name cannot be blank.")
})

model_schema = api.model('ModelSchema', {
    'schema': fields.String(required=True, description="Schema of the model", help="Name cannot be blank.")
})


@ns.route('/ModelSchema')
class ModelSchema(Resource):
    @api.expect(model_key_descriptor)
    @api.response(202, 'ML Schema retrieved.', model_schema)
    def post(self):
        """Returns the schema of a model."""
        json_dictionary = request.json
        print(json_dictionary)

        # Model
        model_name = json_dictionary["name"]
        mode_version = json_dictionary["version"]
        model_format = json_dictionary["format"]

        # Compose the model path
        model_path = 'models/' + model_name + '.' + model_format

        # Local read
        model_dictionary = load(model_path)

        # Make a copy and remove the model from it as non serializable into JSON
        model_dictionnary_copy = model_dictionary.copy()
        del model_dictionnary_copy["model"]
        del model_dictionnary_copy["metadata"]["date"]

        return model_dictionnary_copy


ns = api.namespace('automation/api/v1.0/prediction/generic', description='run any ML models')

model_descriptor = api.model('ModelDescriptor', {
    'path': fields.String(required=True, description="Local path of the model", help="Name cannot be blank."),
    'version': fields.String(required=True, description="Version of the model", help="Name cannot be blank."),
    'format': fields.String(required=True, description="Format of the model", help="Name cannot be blank.")
})

prediction_request = api.model('PredictionRequest', {
    'model': fields.Nested(model_descriptor),
    'features': fields.Wildcard(fields.String)
})

prediction_response = api.model('PredictionResponse', {
    'path': fields.String(required=True, description="Local path of the invoked predictive model",
                          help="Name cannot be blank."),
    'id': fields.String(required=True, description="Uuid of the prediction", help="Name cannot be blank."),
    'prediction': fields.String(required=False, description="The prediction", help="Name cannot be blank."),
    'probabilities': fields.Wildcard(fields.String)

})


@ns.route('/')
class PredictionService(Resource):
    @api.expect(prediction_request)
    @api.response(201, 'Category successfully created.', prediction_response)
    def post(self):
        """Computes a new prediction."""

        try:
            jsonDictionary = request.json
            print(jsonDictionary)

            # Model
            jsonModelDictionary = jsonDictionary["model"]
            modelName = jsonModelDictionary["path"]
            modelVersion = jsonModelDictionary["version"]
            modelFormat = jsonModelDictionary["format"]

            # Features
            jsonPayloadDictionary = jsonDictionary["features"]

            # Compose the model path
            modelPath = 'models/' + modelName + '.' + 'joblib'  # Picking joblib file by default

            # Remote read
            # response = requests.get('https://github.com/ODMDev/decisions-on-ml/blob/master/docker-python-flask-sklearn-joblist-json/models/miniloandefault-rfc.joblib?raw=true')

            # Local read
            dictionary = load(modelPath)

            # Access to the model metadata
            metadataDictionary = dictionary["metadata"]

            # Introspect the signature
            signatureParameters = metadataDictionary["signature"]
            parameterValues = []
            for parameter in signatureParameters:
                print(parameter)
                name = parameter["name"]
                type = parameter["type"]
                value = float(jsonPayloadDictionary[name])
                parameterValues.append(value)

            # Local read
            loaded_model = dictionary['model']

            # Invocation
            invocationMethod = metadataDictionary["invocation"]
            predictedClass = -1
            predictionWrapper = 0

            responseDictionary = {
                "path": modelPath,
                "id": str(uuid.uuid4())
            }

            if invocationMethod == 'predict':
                predictedClass = loaded_model.predict(
                    [parameterValues])
                # Assume an array of a single element to be cast in int
                foundClass = predictedClass[0]
                responseDictionary['prediction'] = foundClass.item()  # cast into int

            if invocationMethod == 'predict_proba':
                predictionWrapper = loaded_model.predict_proba(
                    [parameterValues])

                prediction = predictionWrapper[0]

                # Needs to be generalized
                probabilities = {
                    "0": prediction[0],
                    "1": prediction[1]
                }

                responseDictionary["probabilities"] = probabilities

            # json_string = json.dumps(responseDictionary, indent=4)

            print(responseDictionary)

            return responseDictionary

        except:
            return "KO"


if __name__ == '__main__':
    # Start a development server
    app.run(port=5000, host='0.0.0.0')
