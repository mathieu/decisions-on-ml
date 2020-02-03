# Decision automation on machine learning

This repository includes sample material to show how IBM Decision Services can leverage ML predictive models hosted as micro services.

![Flow](docs/images/ML_microservice_architecture.png "ML microservice stack")

The solution puts in practice in this projet articulates :
- Docker, as a container standard. A precious technology to put in place here in isolation a Python environment,
- Python, the de facto prefered language for ML,
- Flask and Flask-RESTPlus, frameworks bringing web app and RESTfull APIs,
- Pickle, a serialization for Python,
- JobLib, another serialization for Python.

This repository is composed of 3 projects:
- [ML model creation](ml-model-creation/README.md): Several source files to create variations of ML models with scikit-learn to predict a default for a loan repayment. These models are stored in the file system through a pickle serialization or JobLib serialization.

- [A static RESTful ML microservice for scikit-learn models serialized in joblib](ml-model-static-hosting/README.md): A sample of a predictive microservice running a Random Forest Classification model to predict a default for a loan repayment through a joblist serialization. Features values are directly sent as http parameters. The microservice expose an OpenAPI descriptor.

- [A generic REST ML microservice for scikit-learn models](ml-model-dynamic-hosting/README.md): A sample of a lightweight REST/JSON microservice to run multiple sklearn ML models captured as a joblib files.


