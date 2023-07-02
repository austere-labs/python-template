# python template api service

Uses FastAPI, uvicorn and pytest. 

Has simple CI github runner. 

Will build out more stuff over time. 

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

To run tests:  
```
pytest -v
```

If all goes well, for local dev, you should be able to run:  
```
uvicorn app:app --port 8080
```

For Docker:  
```
docker build -t api .
```

```
docker run -p 8080:8080
```
