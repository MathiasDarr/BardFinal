#!/bin/bash

aws cloudformation deploy --stack-name instance-scheudler --template-file instance_scheudler.json --parameter-overrides file://params.properties