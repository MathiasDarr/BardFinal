#!/bin/bash

API_SRC_DIR=watersheds/sauk
API_REPO=bard_api

export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com

docker build -t ${API_REPO} ${API_SRC_DIR}
docker tag ${API_REPO}:latest ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${API_REPO}:latest
docker push ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${API_REPO}:latest