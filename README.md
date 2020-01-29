# decisions-on-ml

## Decision automation on machine learning

This repository includes sample material to show how IBM Decision Services can leverage ML predictive models.

- [HTTP ML microservice for sci-kit learn models serialized in pickle](docker-python-flask-sklearn-pickle/README.md): A sample of a predictive microservice running a sklearn model to predict a default for a loan repayment through a pickle serialization. Features values are directly sent as http parameters.

- [HTPP ML microservice for sci-kit learn models serialized in joblib](docker-python-flask-sklearn-joblist/README.md): A sample of a predictive microservice running a Random Forest Classification model to predict a default for a loan repayment through a joblist serialization. Features values are directly sent as http parameters.

- [REST/JSON ML microservice for sci-kit learn models serialized in pickle](docker-python-flask-sklearn-joblist-json/README.md): A sample of a lightweight REST/JSON microservice to run a sklearn ML model captured as a joblib file.


