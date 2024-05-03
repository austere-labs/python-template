PROJECT_NAME := pythontemplate

lint:
	ruff check .

format:
	black .

test:
	pytest -v -s
	
export-conda:
	conda env export > environment.yml

export-pip:
	pip freeze > requirements.txt

check:
	make lint
	make format
	make test
	make export-pip

start:
	python main.py

docker-build:
	docker build -t $(PROJECT_NAME) .

docker-run:
	docker run -p 8080:8080 $(PROJECT_NAME)

create-env:
	conda env create -f environment.yml -n $(PROJECT_NAME)

# create-kernel:
# 	python -m ipykernel install --user --name pytorch --display-name "Python 3.11 ($(PROJECT_NAME))"

setup:
	make create-env
	pip install -r requirements.txt
	conda activate $(PROJECT_NAME)

