#!/bin/bash

export SERVER_IP=$(docker inspect -f "{{ .NetworkSettings.Networks.ansible_mynet.IPAddress }}" ansible_server_1)
echo ${SERVER_IP}
