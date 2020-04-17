#!/bin/bash
set -e
echo "start building odm-ml..."
echo "current build directory:"
pwd

echo "Building static apps..."
cd ml-service/ml-model-static-hosting
docker build . -t static-ml-microservice  -f ./Dockerfile --no-cache
cd ../../

echo "Building dynamic apps..."
cd ml-service/ml-model-dynamic-hosting
docker build . -t dynamic-ml-microservice  -f ./Dockerfile --no-cache
