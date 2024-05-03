from fastapi.testclient import TestClient
from fastapi import FastAPI
from router import routes

app = FastAPI()
app.include_router(routes)

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to template API service!"}
