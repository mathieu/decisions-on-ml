# Miniloan prediction micro service

A simple example of ML running microservice for real time machine learning based on Python, Flask, scikit-learn and Docker.
On init, a simple SVM model is created and saved on machine. On request arrival for prediction, the SVM model is loaded and returning prediction.    


## Run on Docker

## Build
```console
docker build . -t miniloanpredictionservice  -f ./Dockerfile
```
## Run
```console
docker run -p 3000:5000 -d miniloanpredictionservice 
```

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
http://127.0.0.1:3000/prediction/api/v1.0/loandefault?creditScore=500&income=60000&loanAmount=1000000&monthDuration=120&rate=0.05&yearlyReimbursement=75195
```
You should see the following answer:
```console
[[ 0.46936965 0.53063035]]
```
The predictive service returns the probability for each class, no default and default classes.
With a cut threshold set to 0.5 we expect no payment default in this case.

Send a http request and expect no loan repayment default prediction in this case
```console
http://127.0.0.1:3000/prediction/api/v1.0/loandefault?creditScore=580&income=66037&loanAmount=168781&monthDuration=120&rate=0.09&yearlyReimbursement=16187
```
You should see the following answer:
```console
[[ 0.86797186 0.13202814]]
```
With a cut threshold set to 0.5 we expect a payment default in this case.

Send a http request on the dynamic API and expect a loan repayment default prediction 
```console
http://127.0.0.1:3000/automation/api/v1.0/prediction?model=loan-default-svm&version=1.0&creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195 
```
