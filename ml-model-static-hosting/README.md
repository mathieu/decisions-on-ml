# Miniloan prediction micro service

A simple example of ML running microservice for real time machine learning based on Python, Flask, scikit-learn and Docker.
On request arrival for prediction, a Random Forest Classification model is loaded and run to predict a loan payment default.
Input parameters describing the loan are passed as HTTP parameters. Prediction is returned by the service.

 ![Flow](../docs/images/ml-model-pickle-microservice-architecture.png "ML microservice stack")
 
## Build the ML microservice
```console
docker build . -t miniloanpredictionservice  -f ./Dockerfile
```
## Run the ML microservice
```console
docker run -p 3000:5000 -d miniloanpredictionservice 
```
Your predictive service is ready to predict on the 127.0.0.1:3000 port.
Note that you can run the server without Docker by starting main.py on your local environment. In this case adress will be 0.0.0.0:5000.

## Check
```console
docker ps miniloanpredictionservice 
```
You should see a running container for miniloanpredictionservice image.

## Go to OpenAPI descriptor page

```console
http://127.0.0.1:3000/ 
```
You should see a SwaggerUI layout listing the exposed REST methods.
![Flow](../docs/images/ml-model-stating-hosting-screen-1.png "OpenAPI menu")

Open the predictive method.
![Flow](../docs/images/ml-model-stating-hosting-screen-2.png "Predictive method")

Fill input parameters in the UI to execute the REST endpoint.
![Flow](../docs/images/ml-model-stating-hosting-screen-3.png "Prediction inputs")

Congratulations! You obtained a risk score computed by the scikit-learn ML model.
![Flow](../docs/images/ml-model-stating-hosting-screen-4.png "Prediction results")

From there you can get a loan payment default risk score by sending an HTTP request.

The JSON response returns the probability of a payment default.

You can test the hosted ML method with other parameters and through a curl command.
