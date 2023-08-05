## Super Simple Python Service template...

Uses FastAPI, uvicorn and pytest.

Has simple CI github runner, uses black for formatting and ruff for linting. 
Runner pushes to docker hub. You will need to load your secrets in github for DOCKER_USERNAME and DOCKERHUB_TOKEN respectively. Or set it up per your preference.  

###Please read the Makefile...

It that has **format**, **start**, **test**, **lint**, **check**, **docker-build** and **docker-run** commands respectively. 


Github runner uses these make calls to cohere local dev to the build process. 

Please install Anaconda or Miniconda
[Install Miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html#)

Once you have that installed you can just run setup in Makefile like so: 

```
make setup
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
