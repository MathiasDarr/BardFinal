docker-compose up -d

docker inspect -f "{{ .NetworkSettings.Networks.ansible_mynet.IPAMConfig.IPv4Address  }}" ansible_sshd_1