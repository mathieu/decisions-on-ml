## python-flask-docker-sklearn
A simple example of python microservice for real time machine learning.

On init, a simple SVM model is created and saved on machine. On request arrival for prediction, the SVM model is loaded and returning prediction.    


# Run on docker - local 
docker build . -t {some tag name}  -f ./Dockerfile_local  
detached : docker run -p 3000:5000 -d {some tag name}  
interactive (recommended for debug): docker run -p 3000:5000 -it {some tag name}  


# Use ML api  
http://127.0.0.1:3000/isAlive  
http://127.0.0.1:3000/prediction/api/v1.0/some_prediction?creditScore=397&income=160982&loanAmount=570189&monthDuration=240&rate=0.07&yearlyReimbursement=57195
