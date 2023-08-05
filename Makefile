PROJECT_NAME := indicators

lint:
	ruff --format=github --select=E9,F63,F7,F82 --target-version=py37 .
	ruff --format=github --target-version=py37 .

format:
	black .

test:
	pytest -v
	
export-conda-env:
	conda env export > environment.yml

export-requirements:
	pip freeze > requirements.txt

check:
	make lint
	make format
	make test
	make export-conda-env
	make export-requirements

start:
	uvicorn app:app --port 8080

docker-build:
	docker build -t $(PROJECT_NAME) .

docker-run:
	docker run -p 8080:8080 $(PROJECT_NAME)

setup:
	conda create --name $(PROJECT_NAME) python=3.11
	conda activate $(PROJECT_NAME)
	pip install -r requirements.txt

