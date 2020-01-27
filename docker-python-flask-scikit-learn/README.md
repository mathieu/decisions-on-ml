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
http://127.0.0.1:3000/prediction/api/v1.0/loandefault?creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195
```

Send a http request and expect no loan repayment default prediction in this case
```console
http://127.0.0.1:3000/prediction/api/v1.0/loandefault?creditScore=580&income=66037&loanAmount=168781&monthDuration=120&rate=0.09&yearlyReimbursement=16187
```

Send a http request on the dynamic API and expect a loan repayment default prediction 
```console
http://127.0.0.1:3000/automation/api/v1.0/prediction?model=loan-default-svm&version=1.0&creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195
```
