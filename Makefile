POETRY 	       = poetry run
DC	           = docker compose
DCR			   = $(DC) exec bot
CODE		   = app/

.PHONY: install
install:
	poetry install --no-interaction
	pre-commit install --install-hooks

############ DOCKER ############
.PHONY: build
build:
	$(DC) build

.PHONY: up
up:
	$(DC) up -d
	$(DCR) alembic upgrade head

.PHONY: down
down:
	$(DC) down --volumes

.PHONY: logs
logs:
	$(DC) logs -f
############ DOCKER ############


############ MIGRATIONS #############
.PHONY: migrate
migrate:
	$(POETRY) alembic upgrade head

.PHONY: gen_migration
gen_migration:
	$(POETRY) alembic revision --autogenerate -m $(m)
############ MIGRATIONS #############


############ CODE QUALITY ############
.PHONY: format ## Auto-format python source files
format:
	ruff check --fix
	ruff format

.PHONY: lint ## Lint python source files
lint:
	ruff check
	ruff format --check

.PHONY: typecheck
typecheck:
	$(POETRY) pyright
############ CODE QUALITY ############

############ TESTS ############
.PHONY: test
	$(POETRY) $(TEST) --cov=./ tests/

.PHONY: report
report:
	$(POETRY) $(TEST) tests/ --cov=./ --cov-report html
############ TESTS ############
