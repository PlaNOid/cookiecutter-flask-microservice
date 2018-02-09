.PHONY: dev build up migrate shell dbshell redis-cli test

COMPOSE-DEV = docker-compose -f docker-compose.yml -f docker-compose.dev.yml
COMPOSE-TEST = docker-compose -f docker-compose.yml -f docker-compose.test.yml

dev:
	$(COMPOSE-DEV) up --build

build:
	$(COMPOSE-DEV) build

up:
	$(COMPOSE-DEV) up

stop:
	$(COMPOSE-DEV) down

migrate:
	$(COMPOSE-DEV) exec {{cookiecutter.app_name}} flask db migrate

shell:
	$(COMPOSE-DEV) exec {{cookiecutter.app_name}} flask debug

bash:
	$(COMPOSE-DEV) exec {{cookiecutter.app_name}} bash

dbshell:
	$(COMPOSE-DEV) exec {{cookiecutter.app_name}} flask dbshell

redis-cli:
	$(COMPOSE-DEV) exec {{cookiecutter.app_name}}_redis redis-cli

test:
	$(COMPOSE-TEST) up --build
