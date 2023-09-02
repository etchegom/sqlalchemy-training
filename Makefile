#!make

SHELL := /bin/bash

confirm-erase:
	@echo "This operation will erase stored data. Proceed? (yN) " && read ans && [ $${ans:-N} = y ]

reset: confirm-erase
	@docker compose down -v
	@docker compose up -d --build

pre-commit:
	@pre-commit run --all-files
