## Ansible ##

This directory contains a docker-compose stack for experimenting with ansible.


Enter shell on the ansible client, ensure ability to ssh to the server

Find servers ip address

export server_ip_address=$(docker inspect -f "{{ .NetworkSettings.Networks.ansible_mynet.IPAddress }}" ansible_server_1)
ssh -i ~/.ssh/ansible master@172.16.128.2