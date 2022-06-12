#!/bin/bash

export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

cdk synth --require-approval never
cdk deploy --require-approval never