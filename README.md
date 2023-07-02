# SuperSimple Python api service ...
### to be used as a template to start projects

Uses FastAPI, uvicorn and pytest.

Has simple CI github runner, uses black for formatting and ruff for linting. 

There is a Makefile that has **format**, **start**, **test**, **lint**, **check**, **docker-build** and **docker-run** commands respectively. 

Github runner uses these make calls to cohere local dev to the build process. 

Conda: Make sure you have a conda setup and create a new env:  
```
conda create --name myenv python=3.11
```

Then activate it:  
```
conda activate myenv
```

requirements.txt should be current so you can:  
```
pip install -r requirements.txt
```

To lint:  
```
make lint

```

To run tests:  
```
make test
```

If all goes well, for local dev, you should be able to run:  
```
make start
```

For Docker:  
```
make docker-build
```

```
make docker-run
```
