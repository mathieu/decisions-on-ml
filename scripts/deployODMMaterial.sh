#!/bin/bash
set -e
echo "start ODM material odm-ml..."
echo "current build directory:"
pwd
echo "Deploy XOM..."
curl -k -v -H "Content-Type: application/octet-stream" --data-binary @"./decision-service-projects/Miniloan Service/output/miniloan-xom.jar" -u odmAdmin:odmAdmin http://localhost:9080/res/apiauth/v1/xoms/miniloan-xom.jar

echo "Deploy Ruleapp..."
curl -k -v -H "Content-Type: application/octet-stream" --data-binary @"./decision-service-projects/Miniloan Service/output/miniloanwithml.jar" -u odmAdmin:odmAdmin http://localhost:9080/res/apiauth/v1/ruleapps
