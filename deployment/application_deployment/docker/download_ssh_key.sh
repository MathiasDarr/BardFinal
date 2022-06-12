#!/bin/bash

if [ "$(whoami)" != "root" ]
then
  echo "Script must be run as user: root"
  exit 255
fi

SECRET_NAME=bard/pem

# Check if file already exists

if [ -f "~/.ssh/bard.pem" ]
then
  exit 0
fi

if [ -z $KEY_TEXT ]
then
  export KEY_TEXT=$(aws secretsmanager --region us-west-2 get-secret-value --secret-id ssh/keys --query SecretString --output text | jq -r ".bard")
  echo $KEY_TEXT
fi

echo $KEY_TEXT | base64 -di > ~/.ssh/bard.pem
chmod 600 ~/.ssh/bard.pem

exit 0