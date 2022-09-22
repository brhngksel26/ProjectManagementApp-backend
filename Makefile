.PHONY: stop logs restart bash up clean 

DOCKER-PROJECT-MANAGEMENT=heybooster
DOCKER_MONGO= project-management-mongo


stop:
	docker stop $(DOCKER-PROJECT-MANAGEMENT)
	docker stop $(DOCKER_MONGO)
logs:
	docker logs $(DOCKER-PROJECT-MANAGEMENT) -f --tail 50
restart:
	docker restart $(DOCKER-PROJECT-MANAGEMENT) || true
	docker restart $(DOCKER_MONGO) || true

up:
	cp example.env .env
	docker-compose up -d


