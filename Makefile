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
	docker build -t api .

docker-run:
	docker run -p 8080:8080 api

setup:
	conda env create -f environment.yml

