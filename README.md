# Hosting ML models through micro-services

This part of the repository shows several approaches to serve ML models through a REST API and Docker. 
 
 ![Flow](docs/images/ml-microservice-coo.png "ML microservice stack")

The technologies selected here to fullfill a lightweight machine learning predictive model hosting are:
- Docker, as a container standard, used here to easily build and deploy a Python environment,
- Python, the de facto prefered language for ML,
- Flask and Flask-RESTPlus, frameworks bringing web app and RESTfull APIs,
- Pickle, a serialization for Python,
- JobLib, another serialization for Python.


This repository is composed of 3 projects:
- [ML model creation](ml-model-creation/README.md): Several source files to create variations of ML models with scikit-learn to predict a default for a loan repayment. These models are stored in the file system through a pickle serialization or JobLib serialization.

- [A static RESTful ML microservice for scikit-learn models serialized in pickle](ml-model-static-hosting/README.md): A sample of a predictive microservice running a Random Forest Classification model to predict a default for a loan repayment. The ml model has been serialized with pickle. Features values are directly sent as http parameters. The microservice exposes an OpenAPI descriptor.

- [A generic REST ML microservice for scikit-learn models serialized in joblib](ml-model-dynamic-hosting/README.md): A sample of a lightweight REST/JSON microservice to run multiple sklearn ML models captured as joblib files.


