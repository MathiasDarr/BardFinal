DOCKER_COMPOSE_FILE=docker-compose.yml

all:
	docker-compose -f ${DOCKER_COMPOSE_FILE} up

ssh:
	ssh master@172.16.128.3 -p 22

client_shell:
	docker exec -it ansible_client_1 bash

client_shell:
	docker exec -it ansible_client_1 bash


prune:
	docker-compose down --remove-orphans -v
	docker system prune -f
	docker volume prune -f
