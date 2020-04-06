# Hosting ML models through a micro-service architecture

The technical proposal fits with a concept of operations based on 3 main roles and 4 steps:
 - Step 1: A Data scientist elaborates an ML model in a data science tool.
 - Step 2: A Data scientist exports an ML model serialized in pickle of joblib.
 - Step 3: A developer takes the serialized ML model and hosts it as a microservice
 - Step 4: A Business user creates a decision service in IBM Digital Business Automation that invokes the hosted ML model
 
The machine-learning section of the repository is composed of 2 main parts:
   - ml hosting with microservices
   - sdk to remotely get a prediction from the microservice and manage the ML models


The ML hosting is composed of 3 projects:
- [ML model creation](ml-model-creation/README.md): Several source files to create variations of ML models with scikit-learn to predict a default for a loan repayment. These models are stored in the file system through a pickle serialization or JobLib serialization.

- [A static RESTful ML microservice for scikit-learn models serialized in pickle](ml-model-static-hosting/README.md): A sample of a predictive microservice running a Random Forest Classification model to predict a default for a loan repayment. The ml model has been serialized with pickle. Features values are directly sent as http parameters. The microservice exposes an OpenAPI descriptor.

- [A generic REST ML microservice for scikit-learn models serialized in joblib](ml-model-dynamic-hosting/README.md): A sample of a lightweight REST/JSON microservice to run multiple sklearn ML models captured as joblib files.

The SDK folder includes:
- a ready to use Java SDK,
- the recipe to generate a new SDK with open-api-generator based on the OpenApi description of the ML backend.


