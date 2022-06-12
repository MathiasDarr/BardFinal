#!/bin/bash

UI_SRC_DIR=bridgeburners/fiddler
UI_REPO=bard_ui

export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com

docker build -t ${UI_REPO} ${UI_SRC_DIR}
docker tag ${UI_REPO}:latest ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${UI_REPO}:latest
docker push ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${UI_REPO}:latest