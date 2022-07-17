DOCKER_COMPOSE_FILE=docker-compose.yml

all:
	docker-compose -f ${DOCKER_COMPOSE_FILE} up

ssh:
	ssh master@172.16.128.3 -p 22


shell:
	docker exec -it ansible_client_1 /bin/bash

client_shell:
	docker exec -it --user workstation ansible_client_1 /bin/bash

server_shell:
	docker exec -it ansible_server_1 bash

inventory1:
	bash scripts/inventory.sh

copy_ssh:
	bash scripts/copy_ssh.sh

echo_server_ip:
	bash scripts/server_ip.sh

prune:
	docker-compose down --remove-orphans -v
	docker system prune -f
	docker volume prune -f
