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

## Check
```console
docker ps miniloanpredictionservice 
```
You should see a running container for miniloanpredictionservice image.

## Test the prediction endpoint
Make sure that the service is up and responding.
http://127.0.0.1:3000/isAlive  

Send a http request and expect a loan repayment default prediction 
http://127.0.0.1:3000/prediction/api/v1.0/loanDefault?creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195

Send a http request and expect no loan repayment default prediction in this case
http://127.0.0.1:3000/prediction/api/v1.0/loanDefault?creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195
