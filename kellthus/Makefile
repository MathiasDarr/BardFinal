DOCKER_COMPOSE_FILE?=docker-compose.yaml

COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE)
APPDOCKER=$(COMPOSE) run --rm app
DAKOBED_TAG=latest

prune:
	docker-compose down --remove-orphans -v
	docker system prune -f
	docker volume prune -f

push_ui:
	bash push_ui_image.sh

push_api:
	bash push_api_image.sh

deploy_images:
	bash deploy_images.sh

