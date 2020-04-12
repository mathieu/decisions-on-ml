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
            'path': "models/miniloandefault-xgb-c.joblib",
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


@ns.route('/is-alive')  # Create a URL route to this resource
class HeartBeat(Resource):  # Create a RESTful resource
    def get(self):  # Create GET endpoint
        """Returns an heart beat."""
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

@ns.route('/model-schema')
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
            json_dictionary = request.json
            print(json_dictionary)

            # Model
            json_model_dictionary = json_dictionary["model"]
            model_name = json_model_dictionary["name"]
            model_version = json_model_dictionary["version"]
            model_format = json_model_dictionary["format"]

            # Features
            json_payload_dictionary = json_dictionary["features"]

            # Compose the model path
            model_path = 'models/' + model_name + '.' + 'joblib'  # Picking joblib file by default

            # Remote read
            # response = requests.get('https://github.com/ODMDev/decisions-on-ml/blob/master/docker-python-flask-sklearn-joblist-json/models/miniloandefault-rfc.joblib?raw=true')

            # Local read
            dictionary = load(model_path)

            # Access to the model metadata
            metadata_dictionary = dictionary["metadata"]

            # Introspect the signature
            signature_dictionnary = dictionary["signature"]
            signature_parameters = signature_dictionnary["input"]
            parameter_values = []
            for parameter in signature_parameters:
                print(parameter)
                name = parameter["name"]
                type = parameter["type"]
                value = float(json_payload_dictionary[name])
                parameter_values.append(value)

            # Local read
            loaded_model = dictionary['model']

            # Invocation
            invocation_method = metadata_dictionary["invocation"]

            response_dictionary = {
                "path": model_path,
                "id": str(uuid.uuid4())
            }

            if invocation_method == 'predict':
                predicted_class = loaded_model.predict(
                    [parameter_values])
                # Assume an array of a single element to be cast in int
                found_class = predicted_class[0]
                response_dictionary['prediction'] = found_class.item()  # cast into int

            if invocation_method == 'predict_proba':
                prediction_wrapper = loaded_model.predict_proba(
                    [parameter_values])

                probabilities = prediction_wrapper[0]

                # Needs to be generalized
                probability_dictionnary = {
                    "0": probabilities[0],
                    "1": probabilities[1]
                }

                response_dictionary["probabilities"] = probability_dictionnary

                ## Ok for RFC
                predicted_class = np.where(probabilities == np.amax(probabilities))
                response_dictionary['prediction'] = str(predicted_class[0][0])

            # json_string = json.dumps(responseDictionary, indent=4)

            print(response_dictionary)

            return response_dictionary

        except:
            return "KO"


if __name__ == '__main__':
    # Start a development server
    app.run(port=5000, host='0.0.0.0')
