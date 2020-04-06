# SDK for a ML micro-service

The SDK folder includes:
- a ready to use Java SDK,
- the recipe to generate a new SDK with open-api-generator based on the OpenApi description of the ML backend.

 ![Flow](../docs/images/ml-microservice-coo.png "ML microservice stack")

- [ML model creation](ml-model-creation/README.md): Several source files to create variations of ML models with scikit-learn to predict a default for a loan repayment. These models are stored in the file system through a pickle serialization or JobLib serialization.
