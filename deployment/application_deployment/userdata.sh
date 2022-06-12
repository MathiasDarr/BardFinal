#!/bin/bash

API_REPO=bard_api
UI_REPO=bard_ui

sudo yum -y update
sudo yum -y install ruby
sudo yum -y install wget
cd /home/ec2-user

sudo amazon-linux-extras install docker
service docker start
systemctl enable docker
sudo usermod -a -G docker ec2-user
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com
docker pull ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${API_REPO}/:latest
docker pull ${AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com/${UI_REPO}/:latest