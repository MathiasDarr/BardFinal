#!/bin/bash

export SERVER_IP=$(docker inspect -f "{{ .NetworkSettings.Networks.ansible_mynet.IPAddress }}" ansible_server_1)
echo $SERVER_IP
docker exec ansible_client_1 bash /home/workstation/create_inventory.sh ${SERVER_IP}

