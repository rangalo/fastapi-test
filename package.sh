#!/bin/bash

rm -f fast-api-lambda.zip

mkdir -p lambda-packages

pip install -r requirements.txt  --platform manylinux2014_x86_64 -t ./lambda-packages/ --python-version 3.11  --only-binary=:all:

cd lambda-packages
zip -r9 ../fast-api-lambda.zip . 
cd ..
zip -r fast-api-lambda.zip app/
