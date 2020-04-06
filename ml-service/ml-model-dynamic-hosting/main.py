#!flask/bin/python
import os
import uuid
from flask import Flask, jsonify
from flask import request, jsonify
from flask_restplus import Api, Resource, fields
from flask_restplus import reqparse

import pandas as pd
import numpy as np
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
    'name': fields.String(required=True, description="Name of the model", help="Name cannot be blank.",
                          default='iris-svc'),
    'version': fields.String(required=True, description="Version of the model", help="Name cannot be blank.",
                             default='1.0'),
    'format': fields.String(required=True, description="Format of the model", help="Name cannot be blank.",
                            default='joblib'),
})

model_metadata = api.model('ModelMetadata', {
    'name': fields.String(required=True, description="Name of the model", help="Name cannot be blank."),
    'version': fields.String(required=True, description="Version of the model", help="Name cannot be blank."),
    'format': fields.String(required=True, description="Format of the model", help="Name cannot be blank."),
    'author': fields.String(required=True, description="Author of the model", help="Name cannot be blank."),
    'metrics': fields.Wildcard(fields.String),
    'customProperties': fields.Wildcard(fields.String)
})

model_signature_parameter = api.model('ModelSignatureParameter', {
    'name': fields.String(required=True, description="Name of the model", help="Name cannot be blank."),
    'order': fields.String(required=True, description="Version of the model", help="Name cannot be blank."),
    'type': fields.String(required=True, description="Version of the model", help="Name cannot be blank.")
})

model_signature = api.model('ModelSignature', {
    'input': fields.List(fields.Raw(required=True, description="Inputs", help="Name cannot be blank.")),
    'output': fields.List(fields.Raw(required=True, description="Outputs", help="Name cannot be blank."))
})

model_schema = api.model('ModelSchema', {
    'metadata': fields.Nested(model_metadata),
    'signature': fields.Nested(model_signature),
    'customProperties': fields.Nested(model_metadata),
})

address = api.schema_model('Address', {
    'properties': {
        'road': {
            'type': 'string'
        },
    },
    'type': 'object'
})

person = address = api.schema_model('Person', {
    'required': ['address'],
    'properties': {
        'name': {
            'type': 'string'
        },
        'age': {
            'type': 'integer'
        },
        'birthdate': {
            'type': 'string',
            'format': 'date-time'
        },
        'address': {
            '$ref': '#/definitions/Address',
        }
    },
    'type': 'object'
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
        del model_dictionnary_copy["metadata"]["creationDate"]

        return model_dictionnary_copy


ns = api.namespace('automation/api/v1.0/prediction/invocation', description='run ML models')

request_model_descriptor = api.model('ModelDescriptor', {
    'name': fields.String(required=True, description="Local path of the model", help="Name cannot be blank."),
    'version': fields.String(required=True, description="Version of the model", help="Name cannot be blank."),
    'format': fields.String(required=True, description="Format of the model", help="Name cannot be blank.")
})

prediction_request = api.model('PredictionRequest', {
    'model': fields.Nested(request_model_descriptor),
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
            modelName = jsonModelDictionary["name"]
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
            signatureDictionnary = dictionary["signature"]
            signatureParameters = signatureDictionnary["input"]
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

                probabilities = predictionWrapper[0]

                # Needs to be generalized
                probability_dictionnary = {
                    "0": probabilities[0],
                    "1": probabilities[1]
                }

                responseDictionary["probabilities"] = probability_dictionnary

                ## Ok for RFC
                predicted_class = np.where(probabilities == np.amax(probabilities))
                responseDictionary['prediction'] = str(predicted_class[0][0])

            # json_string = json.dumps(responseDictionary, indent=4)

            print(responseDictionary)

            return responseDictionary

        except:
            return "KO"


if __name__ == '__main__':
    # Start a development server
    app.run(port=5000, host='0.0.0.0')
