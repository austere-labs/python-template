lint: 
	# stop the build if there are Python syntax errors or undefined names
	ruff --format=github --select=E9,F63,F7,F82 --target-version=py37 .
	# default set of ruff rules with GitHub Annotations
	ruff --format=github --target-version=py37 .

format:
	black .

test:
	pytest -v

start:
	uvicorn app:app --port 8080

docker-build:
	docker build -t api .

docker-run:
	docker run -p 8080:8080 api