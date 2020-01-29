# A REST/JSON predictive micro service

A simple example of ML running microservice for real time machine learning based on Python, Flask, scikit-learn and Docker.
On request arrival for prediction, a Random Forest Classification model is loaded and run to predict a loan payment default.
Input parameters describing the loan are passed in JSON as the prediction returned by the service.

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

## Test the prediction endpoint

Make sure that the service is up and responding.
```console
http://127.0.0.1:3000/isAlive  
```

Send a http request and expect a loan repayment default prediction 
```console
http://127.0.0.1:3000/prediction/api/v1.0/loandefault?creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195
```
Running locally the Docker container
```console
curl -d '{"request":{"creditScore":"300","income":"100000","loanAmount":"570189","monthDuration":"240","rate":"0.07","yearlyReimbursement":"57195"}}' -H 'Content-Type: application/json' http://0.0.0.0:3000/automation/api/v1.0/prediction
 ```
 
Running main.py on 0.0.0.0:5000
```console
curl -d '{"request":{"creditScore":"300","income":"100000","loanAmount":"570189","monthDuration":"240","rate":"0.07","yearlyReimbursement":"57195"}}' -H 'Content-Type: application/json' http://0.0.0.0:5000/automation/api/v1.0/prediction
 ```
 
With the following JSON request
```console
{
    "request": {
        "creditScore": "300",
        "income": "100000",
        "loanAmount": "570189",
        "monthDuration": "240",
        "rate": "0.07",
        "yearlyReimbursement": "57195"
    }
}
```
You should receive an answer like
```console
{
    "id": "123",
    "probabilities": {
        "0": 0.6717663255260751,
        "1": 0.32823367447392493
    }
}
```
