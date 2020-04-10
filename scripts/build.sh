#!/bin/bash
set -e
echo "start building odm-ml..."
echo "current build directory:"

ls -la


echo "Building static apps..."
cd ..
cd decision-on-ml/ml-service/ml-model-static-hosting
docker build . -t static-ml-microservice  -f ./Dockerfile --no-cache
echo "Building dynamic apps..."
cd decision-on-ml/ml-service/ml-model-dynamic-hosting
docker build . -t dynamic-ml-microservice  -f ./Dockerfile --no-cache
