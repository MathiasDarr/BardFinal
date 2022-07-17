#!/bin/bash

export SERVER_IP=$(docker inspect -f "{{ .NetworkSettings.Networks.ansible_mynet.IPAddress }}" ansible_server_1)
docker exec --user workstation ansible_client_1 bash /home/workstation/copy_ssh.sh ${SERVER_IP}