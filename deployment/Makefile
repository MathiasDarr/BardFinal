IMAGE=bard/cdk


image: ../deployment/Dockerfile
	docker build . -t ${IMAGE} --build-arg HOME=${HOME}

.PHONY: deploy
deploy: image
	docker run --rm \
	-v ${HOME}/.aws/credentials:/root/.aws/credentials \
	${IMAGE} \
	bash deploy.sh

dev:
	docker run --rm -it \
	-v ${PWD}:/app \
	-v ${HOME}/.aws/credentials:/root/.aws/credentials \
	${IMAGE} \
	bash